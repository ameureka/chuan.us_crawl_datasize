# 导入必要的库
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from pathlib import Path
import re
from urllib.parse import urljoin

async def main():
    # 创建浏览器配置，headless=False 表示可以看到浏览器界面
    browser_conf = BrowserConfig(headless=False)  # or False to see the browser
    
    # 创建爬虫运行配置，设置缓存模式为绕过缓存
    run_conf = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS
    )

    # 使用异步上下文管理器创建爬虫实例
    async with AsyncWebCrawler(config=browser_conf) as crawler:
        # 运行爬虫，访问指定URL
        result = await crawler.arun(
            url="https://chuan.us",
            config=CrawlerRunConfig(
                css_selector="#page > div > div > div > div.content"  # 使用简单的类选择器
            )
        )
        
        # 如果找到了内容，则保存
        if result.markdown:
            # 打印爬取结果的markdown内容
            print("找到的内容：")
            print("-" * 50)
            print(result.markdown)
            print("-" * 50)
            
            # 获取所有文章链接和标题
            print("原始markdown内容：")
            print("-" * 50)
            print(result.markdown)
            print("-" * 50)
            
            articles = []
            for link in result.markdown.split('\n'):
                if 'chuan.us' in link:
                    print(f"处理链接: {link}")
                    # 使用正则提取标题和链接
                    match = re.search(r'\[(.*?)\]\((.*?)\)', link)
                    if match:
                        title = match.group(1).replace('*', '').strip()
                        # 获取原始URL
                        raw_url = match.group(2).replace('<', '').replace('>', '')
                        
                        # 提取文章ID
                        archive_match = re.search(r'archives/(\d+)', raw_url)
                        if archive_match:
                            article_id = archive_match.group(1)
                            # 构建正确的URL
                            url = f"https://chuan.us/archives/{article_id}"
                            articles.append({'title': title, 'url': url})
                            print(f"找到文章: {title} - {url}")

            print(f"\n找到的文章数量: {len(articles)}")
            
            # 创建保存目录
            desktop = Path.home() / "Desktop"
            pachong_dir = desktop / "pachong2"
            pachong_dir.mkdir(exist_ok=True)

            # 遍历爬取每篇文章
            for article in articles:
                try:
                    print(f"\n正在爬取文章: {article['title']}")
                    print(f"URL: {article['url']}")
                    
                    # 爬取文章内容
                    article_result = await crawler.arun(
                        url=article['url'],
                        config=CrawlerRunConfig(
                            css_selector=".entry-content"  # 文章内容选择器
                        )
                    )

                    print(f"爬取结果长度: {len(article_result.markdown) if article_result.markdown else 0}")
                    if article_result.markdown:
                        # 清理文件名（移除不允许的字符）
                        safe_title = re.sub(r'[<>:"/\\|?*]', '', article['title'])
                        # 保存文件
                        file_path = pachong_dir / f"{safe_title}.md"
                        file_path.write_text(article_result.markdown, encoding='utf-8')
                        print(f"已保存文章: {safe_title}")
                    else:
                        print(f"警告：文章 {article['title']} 内容为空")
                
                except Exception as e:
                    print(f"爬取文章 {article['title']} 时出错: {str(e)}")

            print(f"\n所有文章已保存到: {pachong_dir}")
        else:
            print("未找到指定内容")

# 如果直接运行此脚本（而不是作为模块导入）
if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main()) 