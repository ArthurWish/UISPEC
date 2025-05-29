spec_prompt = """
你是UI设计专家。请参考我的页面描述，描述图片中的页面，给出页面的布局结构、基本颜色样式、页面组件结构，必须全面的描述图片中的所有组件。参考描述如下：
                1. 布局结构
界面采用清晰的后台管理系统布局，左侧为导航栏，主体内容区域采用白色卡片式布局，数据展示清晰直观，整体布局简洁大方。

2. 颜色样式
系统使用蓝色作为主色调，搭配红色、绿色、橙色等辅助色彩，涉及到icon时采用红色党建风格。数据卡片使用纯白背景，图表采用蓝粉对比色展示数据，整体配色专业清爽。


4. 页面组件结构
    4.1 顶部导航
从左到右分别是：
系统名称：党建logo+智慧党建系统
组织概览、一级菜单等导航项，分别是一个页签，组织概览选中时为红色
用户信息及通知
    4.2 左侧菜单
数据概览
异常检测
数据分析
实时监管
数据管理等功能模块
排列紧凑，分别由对应icon和菜单名组成菜单项
    4.3 数据总览区
一行包括5个数据卡片，展示党委、党总支、党支部、党小组、党员等核心数据，5个卡片占满一行
每个卡片包含一个对应图标、标题和数值。卡片背景色为玻璃质感渐变色，色彩透明度较高，卡片本身带有阴影
    4.4 组织架构图
    标题为组织名单
以横向的流程图方式展示组织层级关系
每个流程图节点包含编号、名称
通过虚线连接表示上下级关系
主要内容包括：欧尚汽车党委事业部-长安福特党委-长安马自达党委-江北发动机厂党总支-渝北工厂党小组-研发系统党支部-凯程汽车党小组
    4.5 党员分析区
   一行分为两个主要容器，每个容器包括两个图表
左侧容器包括两个部分，左边为党员性别结构环形图，右边为学历分布环形图
右侧容器包括两个表格，左边党员年龄分布表，右侧是党员年龄表
图表配有清晰的图例和数据标注
    4.6 底部操作栏
保存进度、返回、提交等操作按钮，靠右侧
采用蓝色主按钮突出主要操作
请按照这一格式返回你的spec:
```spec
{generated_spec}
"""

code_prompt = '''你是前端代码专家，精通 React、Ant Design 和 Recharts。请根据页面描述，详细还原页面的功能和样式，生成有效的 `App.js` 代码。**请确保代码中不包含多余的多行字符串（""""）或注释**，并使用内联 CSS 样式，不要引用css外部文件。请分步骤思考，确保代码结构清晰且可直接编译。页面描述如下：

{spec_input}
'''

code_prompt_new = """
You are a front-end code expert, proficient in React, Ant Design, and Recharts. Based on the following page description, **fully** replicate the page's functionality and style, and generate valid `App.js` code. 

**Ensure that every component is fully implemented, and do not omit any part**. 

不要使用{/* Left sidebar navigation will go here */}等注释{/**/}来代替代码，这会导致渲染页面失败。

Please use inline CSS styles and make sure the code structure is clear and directly compilable, you must use 'import 'antd/dist/reset.css''. 

Think step by step and implement each part of the page incrementally. The page description is as follows:

'''{spec_input}'''

Please return your answer as the following:

```jsx
{generated_code}
"""

code_prompt_v2 = """
SYSTEM:
You are a senior front-end engineer, expert in React, Ant Design, and Recharts. Apply a “think step by step” approach to ensure each implementation detail is complete and runnable.

TASK:
Based on the page description below, fully replicate every feature and style of the page by generating a working `App.js` file.

CONSTRAINTS:
1. **Completeness**: Do not omit any component, feature, or style.  
2. **No Placeholder Comments**: Do not use comments like `{/* ... */}` in place of real code.  
3. **Styling**: Use inline CSS styles for all layout and design, don't import any css file.  
4. **Imports**: Import all required components from `antd`, `@ant-design/icons`, and `recharts`.  
5. **Code Structure**: Organize components logically (e.g., separate subcomponents if needed) and ensure the final code compiles without errors.

INPUT:
```text
{spec_input}
````

OUTPUT:
Return **only** the complete `App.js` source code in JSX format, for example:

```jsx
// Your fully implemented React code here
```

"""


code_prompt_v3 = """
SYSTEM:
You are a senior mobile front-end engineer, expert in React, Ant Design. Apply a “think step by step” approach to ensure each implementation detail is complete and runnable.

TASK:
Based on the page description below, fully replicate every feature and style of the page by generating a working `App.js` file.

CONSTRAINTS:
1. **Completeness**: Do not omit any component, UI feature.  
2. **No Placeholder Comments**: Do not use comments like `{/* ... */}` in place of real code.  
4. **Imports**: Import all required components from `antd-mobile`, `@ant-design/icons`.  Do not import other external packages.
5. **Code Structure**: Organize components logically (e.g., separate subcomponents if needed) and ensure the final code compiles without errors.
6. **Less Interaction**: Define components with less interaction, display information with static page.

Knowledge Base that You can use:
'antd-mobile' (possible exports: ActionSheet, AutoCenter, Avatar, Badge, Button, Calendar, CalendarPicker, CalendarPickerView, CapsuleTabs, Card, CascadePicker, CascadePickerView, Cascader, CascaderView, CenterPopup, CheckList, Checkbox, Collapse, ConfigProvider, DatePicker, DatePickerView, Dialog, Divider, DotLoading, Dropdown, Ellipsis, Empty, ErrorBlock, FloatingBubble, FloatingPanel, Footer, Form, Grid, Image, ImageUploader, ImageViewer, IndexBar, InfiniteScroll, Input, JumboTabs, List, Loading, Mask, Modal, NavBar, NoticeBar, NumberKeyboard, PageIndicator, PasscodeInput, Picker, PickerView, Popover, Popup, ProgressBar, ProgressCircle, PullToRefresh, Radio, Rate, Result, ResultPage, SafeArea, ScrollMask, SearchBar, Segmented, Selector, SideBar, Skeleton, Slider, Space, SpinLoading, Stepper, Steps, SwipeAction, Swiper, Switch, TabBar, Tabs, Tag, TextArea, Toast, TreeSelect, VirtualInput, WaterMark, createErrorBlock, reduceMotion, restoreMotion, setDefaultConfig, useConfig)
'@ant-design/icons' (possible exports: AccountBookFilled, AccountBookOutlined, AccountBookTwoTone, AimOutlined, AlertFilled, AlertOutlined, AlertTwoTone, AlibabaOutlined, AlignCenterOutlined, AlignLeftOutlined, AlignRightOutlined, AlipayCircleFilled, AlipayCircleOutlined, AlipayOutlined, AlipaySquareFilled, AliwangwangFilled, AliwangwangOutlined, AliyunOutlined, AmazonCircleFilled, AmazonOutlined, AmazonSquareFilled, AndroidFilled, AndroidOutlined, AntCloudOutlined, AntDesignOutlined, ApartmentOutlined, ApiFilled, ApiOutlined, ApiTwoTone, AppleFilled, AppleOutlined, AppstoreAddOutlined, AppstoreFilled, AppstoreOutlined, AppstoreTwoTone, AreaChartOutlined, ArrowDownOutlined, ArrowLeftOutlined, ArrowRightOutlined, ArrowUpOutlined, ArrowsAltOutlined, AudioFilled, AudioMutedOutlined, AudioOutlined, AudioTwoTone, AuditOutlined, BackwardFilled, BackwardOutlined, BaiduOutlined, BankFilled, BankOutlined, BankTwoTone, BarChartOutlined, BarcodeOutlined, BarsOutlined, BehanceCircleFilled, BehanceOutlined, BehanceSquareFilled, BehanceSquareOutlined, BellFilled, BellOutlined, BellTwoTone, BgColorsOutlined, BilibiliFilled, BilibiliOutlined, BlockOutlined, BoldOutlined, BookFilled, BookOutlined, BookTwoTone, BorderBottomOutlined, BorderHorizontalOutlined, BorderInnerOutlined, BorderLeftOutlined, BorderOuterOutlined, BorderOutlined, BorderRightOutlined, BorderTopOutlined, BorderVerticleOutlined, BorderlessTableOutlined, BoxPlotFilled, BoxPlotOutlined, BoxPlotTwoTone, BranchesOutlined, BugFilled, BugOutlined, BugTwoTone, BuildFilled, BuildOutlined, BuildTwoTone, BulbFilled, BulbOutlined, BulbTwoTone, CalculatorFilled, CalculatorOutlined, CalculatorTwoTone, CalendarFilled, CalendarOutlined, CalendarTwoTone, CameraFilled, CameraOutlined, CameraTwoTone, CarFilled, CarOutlined, CarTwoTone, CaretDownFilled, CaretDownOutlined, CaretLeftFilled, CaretLeftOutlined, CaretRightFilled, CaretRightOutlined, CaretUpFilled, CaretUpOutlined, CarryOutFilled, CarryOutOutlined, CarryOutTwoTone, CheckCircleFilled, CheckCircleOutlined, CheckCircleTwoTone, CheckOutlined, CheckSquareFilled, CheckSquareOutlined, CheckSquareTwoTone, ChromeFilled, ChromeOutlined, CiCircleFilled, CiCircleOutlined, CiCircleTwoTone, CiOutlined, CiTwoTone, ClearOutlined, ClockCircleFilled, ClockCircleOutlined, ClockCircleTwoTone, CloseCircleFilled, CloseCircleOutlined, CloseCircleTwoTone, CloseOutlined, CloseSquareFilled, CloseSquareOutlined, CloseSquareTwoTone, CloudDownloadOutlined, CloudFilled, CloudOutlined, CloudServerOutlined, CloudSyncOutlined, CloudTwoTone, CloudUploadOutlined, ClusterOutlined, CodeFilled, CodeOutlined, CodeSandboxCircleFilled, CodeSandboxOutlined, CodeSandboxSquareFilled, CodeTwoTone, CodepenCircleFilled, CodepenCircleOutlined, CodepenOutlined, CodepenSquareFilled, CoffeeOutlined, ColumnHeightOutlined, ColumnWidthOutlined, CommentOutlined, CompassFilled, CompassOutlined, CompassTwoTone, CompressOutlined, ConsoleSqlOutlined, ContactsFilled, ContactsOutlined, ContactsTwoTone, ContainerFilled, ContainerOutlined, ContainerTwoTone, ControlFilled, ControlOutlined, ControlTwoTone, CopyFilled, CopyOutlined, CopyTwoTone, CopyrightCircleFilled, CopyrightCircleOutlined, CopyrightCircleTwoTone, CopyrightOutlined, CopyrightTwoTone, CreditCardFilled, CreditCardOutlined, CreditCardTwoTone, CrownFilled, CrownOutlined, CrownTwoTone, CustomerServiceFilled, CustomerServiceOutlined, CustomerServiceTwoTone, DashOutlined, DashboardFilled, DashboardOutlined, DashboardTwoTone, DatabaseFilled, DatabaseOutlined, DatabaseTwoTone, DeleteColumnOutlined, DeleteFilled, DeleteOutlined, DeleteRowOutlined, DeleteTwoTone, DeliveredProcedureOutlined, DeploymentUnitOutlined, DesktopOutlined, DiffFilled, DiffOutlined, DiffTwoTone, DingdingOutlined, DingtalkCircleFilled, DingtalkOutlined, DingtalkSquareFilled, DisconnectOutlined, DiscordFilled, DiscordOutlined, DislikeFilled, DislikeOutlined, DislikeTwoTone, DockerOutlined, DollarCircleFilled, DollarCircleOutlined, DollarCircleTwoTone, DollarOutlined, DollarTwoTone, DotChartOutlined, DotNetOutlined, DoubleLeftOutlined, DoubleRightOutlined, DownCircleFilled, DownCircleOutlined, DownCircleTwoTone, DownOutlined, DownSquareFilled, DownSquareOutlined, DownSquareTwoTone, DownloadOutlined, DragOutlined, DribbbleCircleFilled, DribbbleOutlined, DribbbleSquareFilled, DribbbleSquareOutlined, DropboxCircleFilled, DropboxOutlined, DropboxSquareFilled, EditFilled, EditOutlined, EditTwoTone, EllipsisOutlined, EnterOutlined, EnvironmentFilled, EnvironmentOutlined, EnvironmentTwoTone, EuroCircleFilled, EuroCircleOutlined, EuroCircleTwoTone, EuroOutlined, EuroTwoTone, ExceptionOutlined, ExclamationCircleFilled, ExclamationCircleOutlined, ExclamationCircleTwoTone, ExclamationOutlined, ExpandAltOutlined, ExpandOutlined, ExperimentFilled, ExperimentOutlined, ExperimentTwoTone, ExportOutlined, EyeFilled, EyeInvisibleFilled, EyeInvisibleOutlined, EyeInvisibleTwoTone, EyeOutlined, EyeTwoTone, FacebookFilled, FacebookOutlined, FallOutlined, FastBackwardFilled, FastBackwardOutlined, FastForwardFilled, FastForwardOutlined, FieldBinaryOutlined, FieldNumberOutlined, FieldStringOutlined, FieldTimeOutlined, FileAddFilled, FileAddOutlined, FileAddTwoTone, FileDoneOutlined, FileExcelFilled, FileExcelOutlined, FileExcelTwoTone, FileExclamationFilled, FileExclamationOutlined, FileExclamationTwoTone, FileFilled, FileGifOutlined, FileImageFilled, FileImageOutlined, FileImageTwoTone, FileJpgOutlined, FileMarkdownFilled, FileMarkdownOutlined, FileMarkdownTwoTone, FileOutlined, FilePdfFilled, FilePdfOutlined, FilePdfTwoTone, FilePptFilled, FilePptOutlined, FilePptTwoTone, FileProtectOutlined, FileSearchOutlined, FileSyncOutlined, FileTextFilled, FileTextOutlined, FileTextTwoTone, FileTwoTone, FileUnknownFilled, FileUnknownOutlined, FileUnknownTwoTone, FileWordFilled, FileWordOutlined, FileWordTwoTone, FileZipFilled, FileZipOutlined, FileZipTwoTone, FilterFilled, FilterOutlined, FilterTwoTone, FireFilled, FireOutlined, FireTwoTone, FlagFilled, FlagOutlined, FlagTwoTone, FolderAddFilled, FolderAddOutlined, FolderAddTwoTone, FolderFilled, FolderOpenFilled, FolderOpenOutlined, FolderOpenTwoTone, FolderOutlined, FolderTwoTone, FolderViewOutlined, FontColorsOutlined, FontSizeOutlined, ForkOutlined, FormOutlined, FormatPainterFilled, FormatPainterOutlined, ForwardFilled, ForwardOutlined, FrownFilled, FrownOutlined, FrownTwoTone, FullscreenExitOutlined, FullscreenOutlined, FunctionOutlined, FundFilled, FundOutlined, FundProjectionScreenOutlined, FundTwoTone, FundViewOutlined, FunnelPlotFilled, FunnelPlotOutlined, FunnelPlotTwoTone, GatewayOutlined, GifOutlined, GiftFilled, GiftOutlined, GiftTwoTone, GithubFilled, GithubOutlined, GitlabFilled, GitlabOutlined, GlobalOutlined, GoldFilled, GoldOutlined, GoldTwoTone, GoldenFilled, GoogleCircleFilled, GoogleOutlined, GooglePlusCircleFilled, GooglePlusOutlined, GooglePlusSquareFilled, GoogleSquareFilled, GroupOutlined, HarmonyOSOutlined, HddFilled, HddOutlined, HddTwoTone, HeartFilled, HeartOutlined, HeartTwoTone, HeatMapOutlined, HighlightFilled, HighlightOutlined, HighlightTwoTone, HistoryOutlined, HolderOutlined, HomeFilled, HomeOutlined, HomeTwoTone, HourglassFilled, HourglassOutlined, HourglassTwoTone, Html5Filled, Html5Outlined, Html5TwoTone, IconProvider, IdcardFilled, IdcardOutlined, IdcardTwoTone, IeCircleFilled, IeOutlined, IeSquareFilled, ImportOutlined, InboxOutlined, InfoCircleFilled, InfoCircleOutlined, InfoCircleTwoTone, InfoOutlined, InsertRowAboveOutlined, InsertRowBelowOutlined, InsertRowLeftOutlined, InsertRowRightOutlined, InstagramFilled, InstagramOutlined, InsuranceFilled, InsuranceOutlined, InsuranceTwoTone, InteractionFilled, InteractionOutlined, InteractionTwoTone, IssuesCloseOutlined, ItalicOutlined, JavaOutlined, JavaScriptOutlined, KeyOutlined, KubernetesOutlined, LaptopOutlined, LayoutFilled, LayoutOutlined, LayoutTwoTone, LeftCircleFilled, LeftCircleOutlined, LeftCircleTwoTone, LeftOutlined, LeftSquareFilled, LeftSquareOutlined, LeftSquareTwoTone, LikeFilled, LikeOutlined, LikeTwoTone, LineChartOutlined, LineHeightOutlined, LineOutlined, LinkOutlined, LinkedinFilled, LinkedinOutlined, LinuxOutlined, Loading3QuartersOutlined, LoadingOutlined, LockFilled, LockOutlined, LockTwoTone, LoginOutlined, LogoutOutlined, MacCommandFilled, MacCommandOutlined, MailFilled, MailOutlined, MailTwoTone, ManOutlined, MedicineBoxFilled, MedicineBoxOutlined, MedicineBoxTwoTone, MediumCircleFilled, MediumOutlined, MediumSquareFilled, MediumWorkmarkOutlined, MehFilled, MehOutlined, MehTwoTone, MenuFoldOutlined, MenuOutlined, MenuUnfoldOutlined, MergeCellsOutlined, MergeFilled, MergeOutlined, MessageFilled, MessageOutlined, MessageTwoTone, MinusCircleFilled, MinusCircleOutlined, MinusCircleTwoTone, MinusOutlined, MinusSquareFilled, MinusSquareOutlined, MinusSquareTwoTone, MobileFilled, MobileOutlined, MobileTwoTone, MoneyCollectFilled, MoneyCollectOutlined, MoneyCollectTwoTone, MonitorOutlined, MoonFilled, MoonOutlined, MoreOutlined, MutedFilled, MutedOutlined, NodeCollapseOutlined, NodeExpandOutlined, NodeIndexOutlined, NotificationFilled, NotificationOutlined, NotificationTwoTone, NumberOutlined, OneToOneOutlined, OpenAIFilled, OpenAIOutlined, OrderedListOutlined, PaperClipOutlined, PartitionOutlined, PauseCircleFilled, PauseCircleOutlined, PauseCircleTwoTone, PauseOutlined, PayCircleFilled, PayCircleOutlined, PercentageOutlined, PhoneFilled, PhoneOutlined, PhoneTwoTone, PicCenterOutlined, PicLeftOutlined, PicRightOutlined, PictureFilled, PictureOutlined, PictureTwoTone, PieChartFilled, PieChartOutlined, PieChartTwoTone, PinterestFilled, PinterestOutlined, PlayCircleFilled, PlayCircleOutlined, PlayCircleTwoTone, PlaySquareFilled, PlaySquareOutlined, PlaySquareTwoTone, PlusCircleFilled, PlusCircleOutlined, PlusCircleTwoTone, PlusOutlined, PlusSquareFilled, PlusSquareOutlined, PlusSquareTwoTone, PoundCircleFilled, PoundCircleOutlined, PoundCircleTwoTone, PoundOutlined, PoweroffOutlined, PrinterFilled, PrinterOutlined, PrinterTwoTone, ProductFilled, ProductOutlined, ProfileFilled, ProfileOutlined, ProfileTwoTone, ProjectFilled, ProjectOutlined, ProjectTwoTone, PropertySafetyFilled, PropertySafetyOutlined, PropertySafetyTwoTone, PullRequestOutlined, PushpinFilled, PushpinOutlined, PushpinTwoTone, PythonOutlined, QqCircleFilled, QqOutlined, QqSquareFilled, QrcodeOutlined, QuestionCircleFilled, QuestionCircleOutlined, QuestionCircleTwoTone, QuestionOutlined, RadarChartOutlined, RadiusBottomleftOutlined, RadiusBottomrightOutlined, RadiusSettingOutlined, RadiusUpleftOutlined, RadiusUprightOutlined, ReadFilled, ReadOutlined, ReconciliationFilled, ReconciliationOutlined, ReconciliationTwoTone, RedEnvelopeFilled, RedEnvelopeOutlined, RedEnvelopeTwoTone, RedditCircleFilled, RedditOutlined, RedditSquareFilled, RedoOutlined, ReloadOutlined, RestFilled, RestOutlined, RestTwoTone, RetweetOutlined, RightCircleFilled, RightCircleOutlined, RightCircleTwoTone, RightOutlined, RightSquareFilled, RightSquareOutlined, RightSquareTwoTone, RiseOutlined, RobotFilled, RobotOutlined, RocketFilled, RocketOutlined, RocketTwoTone, RollbackOutlined, RotateLeftOutlined, RotateRightOutlined, RubyOutlined, SafetyCertificateFilled, SafetyCertificateOutlined, SafetyCertificateTwoTone, SafetyOutlined, SaveFilled, SaveOutlined, SaveTwoTone, ScanOutlined, ScheduleFilled, ScheduleOutlined, ScheduleTwoTone, ScissorOutlined, SearchOutlined, SecurityScanFilled, SecurityScanOutlined, SecurityScanTwoTone, SelectOutlined, SendOutlined, SettingFilled, SettingOutlined, SettingTwoTone, ShakeOutlined, ShareAltOutlined, ShopFilled, ShopOutlined, ShopTwoTone, ShoppingCartOutlined, ShoppingFilled, ShoppingOutlined, ShoppingTwoTone, ShrinkOutlined, SignalFilled, SignatureFilled, SignatureOutlined, SisternodeOutlined, SketchCircleFilled, SketchOutlined, SketchSquareFilled, SkinFilled, SkinOutlined, SkinTwoTone, SkypeFilled, SkypeOutlined, SlackCircleFilled, SlackOutlined, SlackSquareFilled, SlackSquareOutlined, SlidersFilled, SlidersOutlined, SlidersTwoTone, SmallDashOutlined, SmileFilled, SmileOutlined, SmileTwoTone, SnippetsFilled, SnippetsOutlined, SnippetsTwoTone, SolutionOutlined, SortAscendingOutlined, SortDescendingOutlined, SoundFilled, SoundOutlined, SoundTwoTone, SplitCellsOutlined, SpotifyFilled, SpotifyOutlined, StarFilled, StarOutlined, StarTwoTone, StepBackwardFilled, StepBackwardOutlined, StepForwardFilled, StepForwardOutlined, StockOutlined, StopFilled, StopOutlined, StopTwoTone, StrikethroughOutlined, SubnodeOutlined, SunFilled, SunOutlined, SwapLeftOutlined, SwapOutlined, SwapRightOutlined, SwitcherFilled, SwitcherOutlined, SwitcherTwoTone, SyncOutlined, TableOutlined, TabletFilled, TabletOutlined, TabletTwoTone, TagFilled, TagOutlined, TagTwoTone, TagsFilled, TagsOutlined, TagsTwoTone, TaobaoCircleFilled, TaobaoCircleOutlined, TaobaoOutlined, TaobaoSquareFilled, TeamOutlined, ThunderboltFilled, ThunderboltOutlined, ThunderboltTwoTone, TikTokFilled, TikTokOutlined, ToTopOutlined, ToolFilled, ToolOutlined, ToolTwoTone, TrademarkCircleFilled, TrademarkCircleOutlined, TrademarkCircleTwoTone, TrademarkOutlined, TransactionOutlined, TranslationOutlined, TrophyFilled, TrophyOutlined, TrophyTwoTone, TruckFilled, TruckOutlined, TwitchFilled, TwitchOutlined, TwitterCircleFilled, TwitterOutlined, TwitterSquareFilled, UnderlineOutlined, UndoOutlined, UngroupOutlined, UnlockFilled, UnlockOutlined, UnlockTwoTone, UnorderedListOutlined, UpCircleFilled, UpCircleOutlined, UpCircleTwoTone, UpOutlined, UpSquareFilled, UpSquareOutlined, UpSquareTwoTone, UploadOutlined, UsbFilled, UsbOutlined, UsbTwoTone, UserAddOutlined, UserDeleteOutlined, UserOutlined, UserSwitchOutlined, UsergroupAddOutlined, UsergroupDeleteOutlined, VerifiedOutlined, VerticalAlignBottomOutlined, VerticalAlignMiddleOutlined, VerticalAlignTopOutlined, VerticalLeftOutlined, VerticalRightOutlined, VideoCameraAddOutlined, VideoCameraFilled, VideoCameraOutlined, VideoCameraTwoTone, WalletFilled, WalletOutlined, WalletTwoTone, WarningFilled, WarningOutlined, WarningTwoTone, WechatFilled, WechatOutlined, WechatWorkFilled, WechatWorkOutlined, WeiboCircleFilled, WeiboCircleOutlined, WeiboOutlined, WeiboSquareFilled, WeiboSquareOutlined, WhatsAppOutlined, WifiOutlined, WindowsFilled, WindowsOutlined, WomanOutlined, XFilled, XOutlined, YahooFilled, YahooOutlined, YoutubeFilled, YoutubeOutlined, YuqueFilled, YuqueOutlined, ZhihuCircleFilled, ZhihuOutlined, ZhihuSquareFilled, ZoomInOutlined, ZoomOutOutlined, createFromIconfontCN, default, getTwoToneColor, setTwoToneColor)

INPUT:
```text
{spec_input}
````

OUTPUT:
Return **only** the complete `App.js` source code in JSX format, for example:

```jsx
// Your fully implemented React code here
```

"""

code_prompt_mobile_v5 = """
SYSTEM:
You are a senior mobile front-end engineer, expert in React, Ant Design. Apply a “think step by step” approach to ensure each implementation detail is complete and runnable.

CONSTRAINTS:
1. **Component style**: Use position: absolute, mapping to the bbox field in the input.
2. **No Placeholder Comments**: Do not use comments like `{/* ... */}` in place of real code. No code comment like '//'.
3. **Imports**: You can use components from `antd`. Do not import other external packages. Ensure the layout, spacing, typography, colors, and component hierarchy match the screenshot as closely as possible.
4. **Icon and Image**: All icon references use Font Awesome.
5. **Code Structure**: Organize components logically (e.g., separate subcomponents if needed) and ensure the final code compiles without errors.
6. **Less Interaction**: Define components with less interaction, display information with static page.

INPUT:
This is the UI component hierarchy tree corresponding to a UI interface. 
```text
{spec_input}
````

OUTPUT:
Return **only** the complete `App.js` source code in JSX format:

```jsx
// Your fully implemented React code here
```

"""

code_prompt_web_v5 = """
SYSTEM:
You are a senior web front-end engineer, expert in React, Ant Design component, Ant Design ICON, Recharts. Apply a “think step by step” approach to ensure each implementation detail is complete and runnable.

TASK:
Based on the page description below, fully replicate every feature and style of the page by generating a working `App.js` file.
The render page size in 1920 width and 1080 height.
CONSTRAINTS:
1. **Completeness**: Do not omit any component, UI feature.  
2. **No Placeholder Comments**: Do not use comments like `{/* ... */}` in place of real code.
3. **Imports**: Import all required components from `antd`, `@ant-design/icons`, recharts.
4. **Image**: Generate SVG for Image. If the image is in background, use background-image: url().
5. **Code Structure**: Organize components logically (e.g., separate subcomponents if needed) and ensure the final code compiles without errors.
6. **Less Interaction**: Define components with less interaction, display information with static page.

INPUT:
```text
{spec_input}
````

OUTPUT:
Return **only** the complete `App.js` source code in JSX format:

```jsx
// Your fully implemented React code here
```

"""

spec_prompt_web_v5 = """
You are a senior UI-analysis agent.  
Your task: ① receive one UI screenshot, ② infer its visual structure, ③ output **only** a JSON conforming to the “UI Structured Schema v0.2”.  

# 1. Overall rules
- Output must be **valid JSON**, no comments, no extra keys.  
- All coordinates (`bbox`, `background.area`) use the original image size and are **normalized to 0-1**.  
- Colours:  
  • Collect unique foreground / background colours you detect.  
  • Map them to concise token names under `designTokens.colors`, e.g. `"accentBlue"`.  
- Layout grid:  
  • If the design shows column alignment, guess a grid (`columns`, `gap`, `margins`).  
  • Default to 12-column grid if uncertain.  
- Component typing: choose the closest type from  
  `[Page, Card, Image, Icon, Text, Input, TextArea, Button, Checkbox, Radio, Switch,
    Select, Table, List, Grid, Flex, Form, Modal, Drawer, Tab, Tag, Chip, Progress, 
    Avatar, Divider]`.

# 2. Detection detail
For each visible element that conveys meaning:
1. Assign `id` (use kebab-case, prefix with parent when helpful: `login-btn-submit`).  
2. Set `type` from the list above.  
3. Fill `bbox` `{x,y,w,h}`.  
4. **If text is present**, record full `text`.  
5. Detect local colours / radius / elevation only when different from global tokens.  
6. Include child components recursively via `children`.  
7. If a component spans N grid columns, add  
   `"layout": { "gridSpan": N }`.

# 3. JSON root layout
{
  "meta":            { "version": "0.2", "captureSize": { "width": W, "height": H } },
  "designTokens":    { "colors": { … }, "typography": { … } },
  "background":      { "area": {x,y,w,h}, "imageSrc": null | "URL", "description": "…" },
  "layoutGrid":      { "columns": 12, "gap": 16, "margins": 24 },
  "componentTree":   { … }
}

# 4. Output section
Return ONLY the JSON. Do NOT wrap it in markdown or add explanation.

"""

# 提升了CSS
code_prompt_v4 = """

**SYSTEM:**
You are a senior front-end engineer, expert in React, Ant Design, and Recharts. Apply a “think step by step” approach to ensure each implementation detail is complete, functional, and visually appealing.

**TASK:**
Based on the page description below, fully replicate every feature and style of the page by generating two files:

1. A **App.js** file (JSX) that includes all React components and logic.
2. A **index.css** file containing the CSS styles for all components.

**CONSTRAINTS:**

1. **Completeness**: Do not omit any component or feature; ensure everything from the specification is included.

2. **No Placeholder Comments**: Do not use comments like `{/* ... */}` or any other placeholder; provide full implementation details.

3. **Styling**:

   * Use an external CSS file (**index.css**) for all layout and design.
   * Pay close attention to the **visual aesthetics**—ensure the layout is well-aligned, with clean and consistent spacing.
   * Choose colors that enhance the page's attractiveness and ensure they align with the described color scheme. Make sure the visual appeal is **harmonious** and supports readability and engagement.
   * Ensure that the overall design is **balanced**, with properly spaced elements and an aesthetically pleasing flow.

4. **Components**:

   * Ensure the React components are correctly styled using Ant Design components, as well as Recharts where applicable.
   * Pay special attention to visual hierarchy, button sizes, and chart element alignment to make sure the page feels organized and easy to navigate.

5. **Code Structure**:

   * Organize components logically, with clear and intuitive structure (e.g., breaking down complex components into subcomponents where needed).
   * Ensure the layout and design details are addressed systematically, with each piece contributing to a consistent visual theme.
   * Final code should compile without errors and be fully functional.

6. **Less Interaction**: Define components to present static information on the page, with **minimal interaction**. Focus on layout, color, typography, and overall presentation.

**INPUT:**
text
`{spec_input}`

**OUTPUT:**
Return **only** the following two files:

1. **App.css** (JSX):

```jsx
// Your fully implemented React code here
```

2. **index.css**:

```css
/* Your fully implemented CSS styles here */
```

"""

spec_prompt_new = """
You are a UI design expert. Describe the layout, color styles, and component structure of the UI page provided by the user. 

Please provide a detailed description of all components in the graphic, including the styles, layout, and colors of each component, ensuring clarity, accuracy, and conciseness. 

Below is an example of a description specification.

1. **Layout Structure**: The interface adopts a backend management layout, with a navigation bar on the left and a white card-based layout for the main content area, displaying data in a clear and simple manner.

2. **Color Styles**: The primary color is blue, with auxiliary colors including red, green, and orange. Icons use a red党建 (party building) style. The card background is pure white, and the charts use a blue-pink contrast for data visualization.

3. **Component Structure**:
   - **Top Navigation**: Includes system name, navigation menus, user information, and notifications.
   - **Left Menu**: Contains modules like data overview, anomaly detection, data analysis, etc., each with a corresponding icon.
   - **Data Overview Section**: One row contains 5 data cards displaying different data, with glass-like gradient backgrounds and shadows on the cards.
   - **Organizational Structure Diagram**: A horizontal flowchart showing the organizational hierarchy, with dashed lines indicating upper-lower relationships.
   - **Party Member Analysis Section**: The left side includes pie charts for gender and education distribution, and the right side includes tables for age distribution and party member ages.
   - **Bottom Action Bar**: Contains action buttons, with the main button highlighted in blue.
Please return as following:
```spec
{generated_spec}
```
"""

spc_dsx_v1 = """
你是一位经验丰富的UI设计师，擅长从UI截图中精准提取完整的信息，并进行给出尽可能还原的UI描述。请根据提供的UI图片，从以下两个层面全面解析界面内容，并尽可能详细地还原其设计细节与意图：
一、页面级信息分析
请对整个页面进行宏观层面的描述与拆解，包括但不限于以下内容：
整体描述： 
    页面的主要功能或目的（例如：展示型页面、操作面板、用户引导流程等）
    页面所处的产品场景或使用情境（移动端/桌面端、B端/C端、高交互性/静态浏览）
页面构成： 
    页面模块划分（头部、导航、主内容区、侧边栏、底部等）
    各模块之间的层级关系与视觉权重
    主要的信息流路径与用户动线分析
视觉风格： 
    设计风格：是拟物、扁平、Material Design、Neumorphism 还是其他自定义风格？
    色彩体系：主要使用的主色、辅助色、强调色及其用途；是否使用渐变、透明度变化或状态色？
    整体调性：是专业严谨、轻松活泼、科技感、复古风还是其他情绪氛围？
    排版风格：对齐方式（左对齐/居中/右对齐）、网格系统的使用情况

二、组件级信息分析
请识别并列出页面中的各个UI组件，并分别从以下三个维度进行描述：
承载信息 ：组件内展示的实际内容（文字、图标、图片、数据图表等）    
承担的功能 ：组件的作用（按钮用于提交？卡片用于跳转？输入框用于数据录入？）
组件的类型 ：包含的基础组件类型（按钮、输入框、标签、下拉菜单、开关等）和复合组件类型（卡片、模态弹窗、列表项、时间轴、步骤条等）
请严格按照这一格式返回你的spec:
```spec
{generated_spec}
```
"""

spc_dsx_v2 = """
你是一位经验丰富的UI设计师，擅长从UI截图中精准提取完整的信息，并给出尽可能还原的UI描述。

请根据提供的UI图片，从以下的信息维度全面解析UI中的内容，并尽可能详细地还原其设计细节与意图：
**1. UI整体描述：简述UI的整体功能，以及UI所处的产品场景**
**2. 页面构成：对页面进行模块划分（可以划分成头部区域、侧边栏、主体区域、底部区域等，如果没有，则跳过该区域）**
**3. 视觉风格：描述页面的整体调性、色彩体系和设计风格**
**4. 各个区域组件信息分述：对划分出的各个区域进行分开描述，完整描述出其中的全部组件（组件信息应包含组件类型、承担的功能或承载的信息、所处的位置等）**
请注意遵从以下要求：
**1. 组件中的信息应以信息对象模型的形式完整再现，不要省略**
**2. 对于图表类型的组件需要读出图表中的具体数据**
请按照这一格式返回你的spec:
```spec
{generated_spec}
```
"""

spec_mobile = """
你是一位经验丰富的移动端UI设计师，擅长从UI截图中精准提取完整的信息，并给出尽可能还原UI的描述。

请根据提供的UI图片，从以下方面解析UI中的内容，并详细地还原其设计细节与意图：
**1. 页面构成：对页面进行组件划分，可以划分成状态栏、导航栏、页签、卡片列表等**
**2. 各个组件详细描述：对划分出的各个组件进行描述**
**3. 完整描述出其中的全部属性（应包含组件类型、承担的功能或承载的信息、所处的相对位置、边框颜色、背景色、圆角、上下左右间距等）**
请注意遵从以下要求：
**1. 组件中的信息应以信息对象模型的形式完整再现，不要省略**
**2. 所有的文本信息需要准确识别*
请按照这一格式返回你的spec:
```spec
{generated_spec}
```
"""

spc_dsx_v3 = """
You are an experienced mobile UI designer, adept at precisely extracting complete information from UI screenshots and providing the most faithful UI descriptions.

Based on the provided UI image, please comprehensively analyze the UI content across the following dimensions and restore its design details and intent as fully as possible:
**1. Overall UI description:** Briefly summarize the UI’s overall functionality.
**2. Page composition:** Divide the page into modules from top to bottom.
**3. Component information for each module:** Separately describe each identified area, fully detailing all components within it. Component information should include these five aspects: component type, function, contained information, color style and layout, and position.

Please observe the following requirements:
**1.** Information within components must be fully reproduced in the form of an information-object model; do not omit anything.
**2.** Text information should be as detailed as OCR detection.

Please return your answer in the following format:

```spec
{generated_spec}
```
"""

spec_derive_dsx = """
你是一个经验丰富的UI设计师，擅长UI风格和组件布局的衍生设计。
我会向你给出一段UI的文本描述，请你在不改变原有信息结构、功能模块和交互逻辑的前提下，探索新的视觉表达方式与界面组织形式。
你可以改变其中的页面结构、布局、组件类型、视觉风格等（并且请着重改变其中的组件类型），但你仍旧需要输出格式相同的UI描述性文本。
用于衍生的UI文本如下：{spec_input}
请按照这一格式返回你的spec:
```spec
{generated_spec}
```
"""

code_prompt_vue = """
You are a front-end code expert, proficient in Vue, Vue DevUI 组件库和样式. Based on the following page description, **fully** replicate the page's functionality and style, and generate valid `App.vue` code. 

**Ensure that every component is fully implemented, and do not omit any part**. 

Please use inline CSS styles and make sure the code structure is clear and directly compilable. 

Think step by step and implement each part of the page incrementally. The page description is as follows:

'''{spec_input}'''

use context 7.

Please return your answer as the following:

```jsx
{generated_code}
"""


coding_prompt = '''用react和antdesign、recharts尽量细致地还原这一页面,直接返回App.js代码，尽量考虑页面的协调性和精美性,不要修改css。页面描述如下：
                1. 布局结构
界面采用清晰的后台管理系统布局，左侧为导航栏，主体内容区域采用白色卡片式布局，数据展示清晰直观，整体布局简洁大方。

2. 颜色样式
系统使用蓝色作为主色调，搭配红色、绿色、橙色等辅助色彩，涉及到icon时采用红色党建风格。数据卡片使用纯白背景，图表采用蓝粉对比色展示数据，整体配色专业清爽。

3. 文案内容
内容以党建管理相关的数据统计为主，包括党委、党总支、党支部等组织架构数据，以及党员性别、学历、年龄等维度的统计分析。文案风格简洁规范。

4. 页面结构
    4.1 顶部导航
从左到右分别是：
系统名称：党建logo+智慧党建系统
组织概览、一级菜单等导航项，分别是一个页签，组织概览选中时为红色
用户信息及通知
    4.2 左侧菜单
数据概览
异常检测
数据分析
实时监管
数据管理等功能模块
排列紧凑，分别由对应icon和菜单名组成菜单项
    4.3 数据总览区
一行包括5个数据卡片，展示党委、党总支、党支部、党小组、党员等核心数据，5个卡片占满一行
每个卡片包含一个对应图标、标题和数值。卡片背景色为玻璃质感渐变色，色彩透明度较高，卡片本身带有阴影
    4.4 组织架构图
    标题为组织名单
以横向的流程图方式展示组织层级关系
每个流程图节点包含编号、名称
通过虚线连接表示上下级关系
主要内容包括：欧尚汽车党委事业部-长安福特党委-长安马自达党委-江北发动机厂党总支-渝北工厂党小组-研发系统党支部-凯程汽车党小组
    4.5 党员分析区
   一行分为两个主要容器，每个容器包括两个图表
左侧容器包括两个部分，左边为党员性别结构环形图，右边为学历分布环形图
右侧容器包括两个表格，左边党员年龄分布表，右侧是党员年龄表
图表配有清晰的图例和数据标注
    4.6 底部操作栏
保存进度、返回、提交等操作按钮，靠右侧
采用蓝色主按钮突出主要操作'''

check_prompt = '''
我有一个react的app.js代码，这个代码使用antdesign和recharts库实现了一个页面，但是运行存在一些报错，你需要根据我给出的报错修改代码，并审查代码中是否存在其他的的问题并修正,返回修改后的正确app.js代码。
注意，尽量保持原页面的组件结构，尽量不要导入额外的包。
你的返回应该是
```jsx
{generated_code}
'''

improve_prompt = '''
我有一个react的app.js代码，这个代码使用antdesign和recharts库实现了一个页面，但是这个代码渲染出的页面可能有些布局或样式问题，例如无法对齐，组件使用错误，或是背景色冲突等。
注意，你可能会发现一些图片渲染缺失，这种问题不需要考虑，你需要根据我给出的渲染图分析错误，修改代码,返回修改后的app.js代码。
注意，尽量保持原页面的组件结构，可以从ant-design/icons导入icon，但不要导入css，内部嵌入样式即可。
你的返回应该是
```jsx
{generated_code}
'''
rag_prompt = '''
你可以参考相关组件的写法，例如，对于表格组件，可以参考：//
 1. 引入 Table 和相关组件
import { Table, Tag, Avatar, Dropdown, Button } from 'antd';
import { EllipsisOutlined } from '@ant-design/icons';

// 2. Mock 数据：团队列表
const teamListData = [
  {
    key: '1',
    avatar: 'https://via.placeholder.com/40',
    teamName: '研发部',
    role: '管理员',
    email: 'dev@company.com',
    status: 'active',
    joinDate: '2022-03-15',
  },
];

// 3. 列配置
const teamColumns = [
  {
    title: '团队',
    dataIndex: 'team',
    key: 'team',
    render: (_, record) => (
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <Avatar src={record.avatar} />
        <span style={{ marginLeft: 12 }}>{record.teamName}</span>
      </div>
    ),
  },
  { title: '角色', dataIndex: 'role', key: 'role' },
  { title: '联系邮箱', dataIndex: 'email', key: 'email' },
  {
    title: '状态',
    dataIndex: 'status',
    key: 'status',
    render: status => (
      <Tag color={status === 'active' ? 'green' : 'blue'}>
        {status === 'active' ? '已加入' : '待确认'}
      </Tag>
    ),
  },
  { title: '加入时间', dataIndex: 'joinDate', key: 'joinDate' },
  {
    title: '操作',
    key: 'action',
    render: () => (
      <Dropdown overlay={teamActionsMenu} trigger={['click']}>
        <Button type="link" icon={<EllipsisOutlined />} />
      </Dropdown>
    ),
  },
];

// 4. 在 JSX 中使用 Table
<Table
  dataSource={teamListData}
  columns={teamColumns}
  pagination={{ pageSize: 5 }}
  rowKey="key"
/>

'''

base_spec_propmt = """
你是一位经验丰富的UI设计师，擅长从UI截图中精准提取完整的信息，并给出尽可能还原的UI描述。
请按照这一格式返回你的spec:
```spec
{generated_spec}
"""
