本文最初于 2021年 3月13号发布于笔者的微信公众号。
多年前笔者在学习 UNIX 操作系统时，遇到一个词叫做 ＲＴＦＭ （ 据称是英文 Read The Fine Manual ，“请阅读那本精致的说明书” 的缩写) . 因为新人对于系统的使用总是有各自各样的疑惑和不懂，老人每次都要重复解释，会觉得很烦，所以会告诉新人去读说明书，就是 RTFM 。当然也有人说 F 是别的词的缩写，这里就不展开讨论了。
问：有没有快速入门以太坊 ( Ethereum, 或缩写为 eth ) 的方法？ 答：没有。建议先把 btc 搞懂有了基础后，再来研究 eth, 会容易一些。请参见笔者老文章 “王川：关于 btc 的 RTFM”
问：有没有什么好的介绍 eth 的入门书籍和信息来源？ 答：1/ Mastering Ethereum: Building Smart Contracts and DApp, by Andreas M. Antonopoulos & Gavin Wood, 2018年十一月出版，2021 年三月再版 2/ The Infinite Machine: How an Army of Crypto-hackers Is Building the Next Internet with Ethereum, by Camila Russo， 2020年七月出版 3/ How to DeFi, by CoinGeicko, Darren Lau, 2020 年三月出版.
亚马逊 kindle 上都可以直接买到这些电子书。因为以太坊技术更新速度快，很多书籍内容很快过时，建议关注下面一些网站来追踪最新信息。
1/ etherscan. io 这是研究以太链上各种实时信息的最全面最细的门户网站 2/ ethereum.org, 这是以太坊各种入门信息的网站。 3/ vitalik.ca, 这是以太坊创始人之一 Vitalik Buterin 的网站，里面有各种相当深入的技术讨论 4/ https://github.com/ethereum/EIPs 可以直接看到以太坊各种改进建议 (EIP) 的原始信息。 5/ defipulse.com, 这是研究 defi 方面信息的一个综合网站。 6/ consensys.net , consensys 是最早支持以太坊的各种基础设施的比较知名的软件公司 7/ messari.io 这是在区块链行业研究做得最深的公司之一。 8/ coingecko.com， 这是区块链各种实时价格信息的入口网站。 9/ ethhub.io 这是一个汇集各种以太坊信息文档的网站。
问：关于 eth 方面的最新信息, 有哪些可以追踪的人？ 答：在 youtube 上， 可以关注这些频道： Bankless, Andreas Antonopoulos， 推特上: @VitalikButerin,@BanklessHQ, @sassal0x, @AndreCronjeTech, @RyanWatkins_, @RyanSAdams，@TrustlessState， @haydenzadams, @zksync, @ethereumJoseph，@hasufl, @qwqiao
问：btc 和 eth 的主要区别是什么？ 答：除了加密算法，出块速度，通胀率等区别之外。btc 设计上刻意不支持图灵完备的计算，比如说编程里面的 for loop. 而以太坊在设计上就是要支持图灵完备的计算，这样可以实现复杂的智能合约。
再往深处说，btc最大优点是不变，任何群体无法单方面改变协议，过去十二年的良好运营记录也验证了这一点。eth 社区则是定期会更新一些软件协议，优化平台效率, 让平台变得更好。以太代码里有所谓“难度系数的炸弹”，这样强迫一定时间后，矿工跟着社区的硬分叉走，所以矿工在以太社区里面，相对而言是弱势群体。这种区别，反应了针对不同应用场景的不同设计思路，不能简单的说谁好谁坏。
问：智能合约是什么？ 答：请参见下面链接 https://nakamotoinstitute.org/the-idea-of-smart-contracts/ 关于智能合约愿景的文章，作者 Nick Szabo.
另外参见下面链接，关于“区块链和社会可扩展性”的文章， 作者也是 Nick Szabo. http://unenumerated.blogspot.com/2017/02/money-blockchains-and-social-scalability.html
问：eth 通胀率是多少？ 答：eth 现在总量约 1.15 亿，目前大约每 13-14 秒出一个块，每一个块会新增两个 eth，再加上所谓 “uncle block reward”, 每年新增 eth 数目接近五百万。2021年七月份的 London 硬分叉会实施所谓 EIP-1559, 销毁部分 eth, 可能大幅度降低通胀率。另外最终实施的 eth 2.0 可能会把年通胀率长期保持在一个较低 (低于 1%）的水平。以太坊平台的发展思路是 Minimum Viable Issuance, 就是说在保证平台安全稳定的前提下，不断减少新增发的 eth 的数目。从以太坊2015年七月主网上线以来的运营记录看，是完全兑现这个承诺的。
问：eth 上什么钱包软件最好？ 答：最流行的是 Metamask,中文社区俗称小狐狸，据称 2020年十月有一百万个月活用户。其它钱包软件选择，参考
https://ethereum.org/en/wallets/ 软件安全管理是个大课题，需要非常谨慎，不能有任何想当然。
问：eth 有什么风险？ 答：风险很多。已知的风险包括：钱包软件管理风险，黑客操纵预言机价格偷钱的风险，自己瞎折腾耗费很多 gas 亏钱的风险，项目方利用智能合约漏洞卷款逃跑的风险，挖矿的所谓“无常损失”的风险。未知的风险，更是不计其数。
问：Defi 是什么，如何入门 Defi, 挖矿 ? 答：除了上面的书籍和网站以外，建议自己先搜一下，研究理解这几个主要的 defi 项目的运作机制：uniswap, makerdao, compound, aave, yearn.finance。各种新项目层出不穷，很难迅速判断前景。不要着急想赚钱，先去理解大部分人是怎么亏钱的。可能有很多项目在裸泳，但只有退潮的时候才能完全看清。另外请参见笔者的文章 “王川：去中心化的流动性黑洞, 和区块链第一法则”
问：NFT 是什么? 答：NFT 是 Non-Fungible Token 的缩写。参见
https://ethereum.org/en/nft/ 的介绍。
最近有位叫 Beeple 的艺术家，把自己的一幅艺术作品放到以太链上，并在三月十一号通过拍卖行 Christie’s 拍出六千九百万美元的天价。有兴趣的人可以直接上网搜索相关智能合约和钱包地址去理解相关逻辑。这个行业还在极早期，大家都是瞎子摸象，摸得非常开心激动，但没有人知道最终会演变成什么样子。
问：以太坊上费用好贵啊，什么人会去用？ 答：硅谷的小破黑屋，房价好贵啊，什么人会去住？另外请参见笔者的文章
“王川：以太坊的费用，为什么这么高？”
问：以太坊 2.0 是什么东西？ 答：参见：https://ethereum.org/en/eth2/ 关于以太坊 beacon chain 的信息，请参见：https://beaconscan.com/ https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-phases/ https://launchpad.ethereum.org/
问：这么难懂，这么多风险，费用又这么贵，什么人吃饱撑了会去搞以太坊？ 答：火好烫啊，会烧毁房屋，烧死人，什么人吃饱撑了会去用火？电好可怕啊，高压电可以电死人，什么人吃饱撑了会去用电？火车噪音好大啊，又喷那么多黑烟，什么人吃饱撑了会修铁路开火车？
问：以太坊究竟能干什么？ 答：凡是需要第三方中介机构来仲裁，协调或者清算的社会功能，都有可能被以太坊替代，因为前者效率太低下了，而且常常掉链子。另外，不要只看它现在可以做什么，而要思考它未来可能做哪些现在根本做不了的事情。参见笔者老文章 “王川：为什么思维模型是最重要的财富 （一）”
问：读这些资料好累好累，可是我就想速成，有没有捷径？ 答：RTFM !
