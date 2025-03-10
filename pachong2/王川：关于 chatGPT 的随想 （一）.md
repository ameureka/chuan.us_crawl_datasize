本文是 [**王川: 关于 GPT-3 的随想 （一）**](https://chuan.us/archives/<https:/chuan.us/archives/155>) 的续篇。
1/ 过去三个多月，大部分人都已经听到各种关于 chatGPT 的铺天盖地的消息了。如果你还不清楚，chatGPT 作为一种基于人工智能的用自然语言实现人机对话的工具，可以帮助你：
一本正经的写诗，小说，剧本；帮助学生做作业，写论文； 写出一份看上去还不错的商业计划书；写各种捣浆糊的软文; 根据自然语言指示，直接生产高质量的代码, 用户界面设计 ; 通过了医生和律师资格考试 ； 翻译上万字的英文书籍到其它文字，据说翻译质量有些地方已经超过人工。
衍生的应用包括上传 pdf 文档后，自动读取信息，帮你提供总结，迅速回答关于此文的各种问题， 等等。
2/ 这个新工具的涌现是如此之快，以至于，不管现在的文章描绘什么样的功能，估算什么样的成本和费用， 再过几个月，大概率会变得更好。
3/ 根据各方面信息的综合， 从 Gpt-3 到 chatGPT 在技术上的改进，主要不在于训练参数的增加，而在于对其进行对话方面的专门培训。这里有个概念叫做 “人工反馈增强学习” ( Reinforcement Learning from Human Feedback, 简称 RLHF ). 简而言之，就是每次模型生成文本，用人工反馈作为性能衡量标准，优化模型。RLHF 实践的第一个挑战是人工反馈成本相对比较昂贵; 第二是不同的人对同样的输出可能会有不同的反馈，让语言模型无所适从。正确使用社交媒体，也可以看成是对自己的 RLHF. 粉丝越多，获取反馈的成本就越低，这样培训自己的成本也越低，进步也越快。( 当然需要注意的是，迅速拉黑没有任何价值的，不友好的反馈和抬杠. )
4/ AI 的算力成本主要分两部分，一部分是训练成本，一部分是推理 (inferencing). 训练成本好比把一个小孩从生下来到 22岁大学毕业的教育成本。而推理成本好比要给大学毕业生支付工资，让他来帮你做事。微软 / Openai 对于 Chatgpt 之类模型的具体训练和推理成本采取了一个刻意模糊和语焉不详的态度，大概是不想让竞争者知道太多实质性细节。从公开信息里大概可以了解到微软在 Openai 的计算上至少投入了一万台 GPU，和价值十亿美元以上的算力成本。
5/ 二月九号网上有 Dylan Patel 为第一作者的文章 “Inference cost of search disruption – LLM cost analysis” 分析，基于日活用户一千三百万的分摊成本，算出 open-ai 提供的推理服务的硬件成本大约每天 $694000 (需要 28936 个 gpu)， 每个搜索成本在 0.36美分左右。文章分析如果谷歌给普通用户提供同质的大语言模型的搜索服务，每年将增加三百六十亿美元的推理成本，这是它目前不愿意做的。
6/ 另一方面， openAI 三月一号推出的最新的对于 chatGPT API 调用的价格，每一千个词的输入处理只要 0.002 美元。反推的结论，就是目前其边际成本应当是略低于这个价格。实际成本数据估计非常复杂。但有一点可以确定，单位边际成本每个月都会下降。任何估算数字，你看到的时候，已经过时，高于实际成本了。
7/ chatGPT 现在给普通用户提供每个月 20 美元的付费服务，称之为 chatGpt plus. 但 openAI 的主要营收，应当是来自给开发者和企业提供的 chatGPT API 服务。早期的企业客户包括 Snapchat, Instacart 和 Shopify. 著名对冲基金 Citadel 创始人几天前宣布正在和 OpenAI 磋商购买整个企业内部使用 chatGPT API 的软件许可证。有超过一千万日活用户的即时通讯软件 Slack， 也宣布已经把 chatGPT 的功能整合到自己的软件里了。
8/ 推特上有一位网名叫 debarghya_das 的作者三月二号发布了一个计算 openAI 的收入和利润的非常粗略的模型。算下来每小时的 A100 GPU 带来的收入是其成本的至少 2.1倍，一万张 GPU 一年带来的收入超过两亿美元。现阶段，openai 的主要策略应当是不断降价以吸引更多的开发者进入其生态系统，分摊算力成本，利润多少相对次要。
9/ 一个参考数据：2022年 AWS 的云计算收入大约八百亿美元 (2015年是八十亿美元), 有机构估算，全球云计算市场规模到 2029年预计达 1.7 万亿美元。openai 作为AI 市场领先者，来自 chatgpt API 的收入五年内突破十亿， 五十亿美元，甚至更高的可能性存在。目前暂时看不到天花板。另外一个数据可以比较：微软 2016 年以二百六十亿美元的价格收购 LinkedIn. 后者被微软收购后，在 2022 年的年收入就达到一百四十亿美元 . OpenAI 被用户追捧的热度和产品发展的潜力，显然远大于 LinkedIn. 有了微软的销售渠道，收入和利润潜力的想象空间，自然大很多。这里还有两个关键，最大的开发者社区， 拥有一亿活跃用户的 Github （远超所有其它竞争者）， 它的主人是微软；而微软的云服务 Azure, 在全美市场份额占 23%， 仅次于 AWS. 在 Github 上开发人工智能应用，调用 chatGpt 的API, 再顺手部署到 azure 的云服务上，将成为大部分第三方开发者阻力最小的选择。
10/ OpenAI 积累了几个季度的营收数据后，可能到 2024年的某个时段择机上市。当下的营收数据没有那么重要，只要能够显示出强劲的市场需求和增长，只要有投行愿意画大饼，勾勒出营收突破五十亿美元的路线图， 那么大概率有足够多热钱愿意为之买单，支持二十倍营收，也就是至少一千亿美元的市值。
11/ openAI 如果成功上市，在 2015年的原始几家风险投资机构的回报，可能达到 50 -100 倍以上。他们一定拿着这个业绩去四处吹嘘，向机构投资者融资建立更大，几十亿，上百亿美元级别的，专门投资人工智能和相关应用的基金。
12/ 微软是 openAI 的股东之一，和 openAI 有比较复杂的利润分成协议，但基本上在 chatGPT 的问题上，可以把他们两家看成是一体的。微软会把此技术和其生态内其它工具如 Bing, Edge 浏览器, Office，Github, Azure 等牢牢绑定，帮助建立用户习惯和依赖性, 扩大生态圈的影响力。微软有先发优势，规模成本优势和渠道优势。对于大多数用户和软件服务商而言，投入微软的怀抱，将是阻力最小的演化方向。
13/ 除了微软之外, 英伟达（Nvidia），台积电 (TSMC）这两家公司是这波浪潮的直接受益者。英伟达 2021 年在 GPU 市场的份额超过 80%, 并且有强大的 CUDA软件开发生态。台积电 2021 年在全球晶圆代工厂的市场份额超过 50%.
14/ chatGPT 语言模型的生成，微软在 Openai 的计算上至少投入了一万台 GPU, 所以如果没有上亿美元的原始投资，外人不可能在算力上和 chatGpt 直接竞争. 这还不包括需要获取海量的数据用于培训，软件工程师调算法模型等成本。 chatGpt 本身也在不断进步，创业公司要想另起炉灶和微软展开军备竞赛，GPU 的投入是不能省钱的。Nvidia 的销售人员也一定会给你足够多的鼓励。人工智能的风投基金，最后相当比例的钱一定会去购买 Nvidia 的 GPU ；这正如 web2 风投的钱，相当比例去谷歌脸书打广告 ；web3 风投的钱，相当比例去以太坊上变成 gas 烧掉。
15/ 人工智能的本质，就是做大量的矩阵乘法计算，这是大学里线性代数的必修课。如果要把军备竞赛升级，那就要去做自己的专用人工智能芯片，做一些专门的优化，以期待在算力成本上超越现有的 GPU．谷歌搞了自己的 TPU，特斯拉有 dojo．但要在单位算力成本上超越年收入两百亿美元的 Nvidia，一定要有巨大的生产规模，这是普通小公司无法参与的游戏。不管谁做自己的专用芯片，最后大概率会投入台积电的怀抱。台积电在亚利桑那州建造的晶圆代工厂，一定要忙死了。
16/ chatGPT 的主要收入来源是财大气粗的企业用户。微软的 Azure 2022年下半年在云计算上的收入是四百一十亿美元，在云计算的市场份额上大约是谷歌的两倍。chatGPT 的很多功能可极大提高企业用户的效率，openAI 已经在和咨询公司 Bain 合作，用 chatGPT 的技术帮助可口可乐提高市场营销和运营的效率。这个趋势只是刚刚开始。这一方面可以增加微软的云计算的营收，另一方面可以分摊算力的成本，在单位算力成本上拉大对谷歌的优势，并以此进一步扩大其云计算的市场份额。微软的另外一块主要业务，“Productivity and Business Process”, 2022 年下半年的收入为三百三十亿美元，包含 Office suite, ERP, LinkedIn 等服务，这块业务也同样将大大受益于 chatGPT 的技术，增加营收，帮其分摊算力成本。
17/ chatGPT 可能直接颠覆”搜索点击广告“的商业模式。谷歌的收入超过 80%来自搜索广告业务，如果直接用同样的方式来迎接微软的挑战，新增的算力成本会大幅度减少利润。而微软本来在搜索领域市场份额就很低，可以完全不考虑盈利来获取搜索的市场份额。另一方面，随着 chatGPT 的功能的持续进步，网上用户使用习惯可能会慢慢脱离”搜索为主“的模式，而最终将搜索的商业模式边缘化。谷歌将处于一种 “Damned if I do, damned if i donot ” ( 伸头也是一刀，缩头也是一刀）的尴尬状态。
18/ OpenAI 成功上市后会促进大笔热钱涌入，短期内制造更多 AI 领域的需求，部分公司营收增速极快，推高估值，对整个行业造成一波又一波的水涨船高的效应，在某个时间段内会产生“所有人都在发财，再不加入我就晚了”的错觉。但大部分投资者最终都会在此领域亏钱，因为：一，所投的企业的竞争优势狭隘且短暂，很容易突然被新来的竞争者赶上并淘汰。二，所投企业的利润来源本身就是风投带来的热钱支持的企业，一旦风投资金增量减缓甚至萎缩，营收和利润萎缩也很快。三，投资时往往企业的 PE 值已经很高，把未来四五年的最乐观的预期增长情况都算进去了，一旦增速低于预期，市值很容易大幅下跌。
19/ 投资高科技不等于发大财，散财的几率其实超过 90%。只有在高科技可以让极少数公司获得全面的垄断性时，这才可能发财。津津乐道高科技，而不讨论它是否, 以及如何能带来权力和垄断，那就是 “连错都谈不上” ( not even wrong). 可以参考笔者的老文章 [**王川: 从权力和垄断的演化机制，看投资(一）**](https://chuan.us/archives/<https:/chuan.us/archives/868>)
20/ 极少数核心竞争力不在 AI 领域之内，但五到十年内不可能被 AI 所替代，可以利用 AI 大幅度提高效率，增收节支，强化其核心竞争力和垄断性的企业，也会是这波 AI 浪潮的赢家之一。九十年代后期互联网兴起时，一些传统消费类的企业如 Proctor & Gamble, Walmart, Coca cola, 就是这样的例子。这一次有哪些类似的赢家，需要慢慢观察。
21/ 但chatGPT 的意义远不在此。很多需要高技能的行业人员 (从程序员到律师，到游戏设计， 翻译等等) 反映使用此工具对效率的提高从 30%到 80% 不等。这还只是序曲。这个工具本身还在加速变得更好。各行各业的效率的提高还会不断组合叠加。
22/ 可以比较的是，瓦特 1776年推出可商用的蒸汽机，到1804年英国首次出现蒸汽机推动的火车，间隔28年。按照沃顿商学院教授 Ethan Mollick 的说法，十九世纪初美国的各类小工厂采用蒸汽机后，效率普遍提高 25%. 1776年的美国人根本无法想象和理解，将近一百年后铁路贯通美洲大陆对经济模式和社会结构的革命性影响。1885年成立的斯坦福大学， 其初期主要资金，就是来自铁路大亨的财富。
23/ chatGPT 已经开始对各行各业产生立竿见影的，比当年蒸汽机还要更大的效率提升，这意味着 AI 对人类社会的巨大影响将注定远超蒸汽机在十九世纪的影响。AI 时代的“火车”的涌现， 我们无需等待 28年，它将超越现在所有人最狂野的想象。
(未完待续）
——-
**作者简介：****王川,投资人,现居加州硅谷。****微信号9935070, 推特号”Svwang1″, 新浪微博****“硅谷王川”, 网站 chuan.us. 所有文章表达作者个人观点仅供参考，不构成对所述资产投资建议，投资有风险，入市须谨慎.**
**在投资和创业的道路上如何集思广益，举重若轻？****欢迎加入王川的俱乐部, 这是一个聚集世界各地各行各业，有着独立思考和独特视角的精英的高端收费社区.****详情请点击下面文章连接**
[**RTFM – 关于投资俱乐部的使用说明 ( 第二版）**](https://chuan.us/archives/<https:/chuan.us/club>)
有意申请入会者请和王川（微信号: 9935070 或推特 “svwang1” 私信) 直接联系。
