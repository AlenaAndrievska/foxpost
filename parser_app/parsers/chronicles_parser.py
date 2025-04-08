import datetime
import time

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }

chronic_ukraine_parser_urls_01 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-12-03T14:13&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-11-24T15:41&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-11-14T06:09&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-11-01T15:21&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-10-22T14:40&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-10-13T15:09&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-10-06T15:37&d=DESC',]

chronic_ukraine_parser_urls_02 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-09-26T18:33&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-09-20T19:12&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-09-12T19:51&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-09-06T12:28&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-08-27T14:27&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-08-16T18:42&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-08-12T13:13&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-08-03T05:38&d=DESC',]

chronic_ukraine_parser_urls_03 = [ 'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-07-29T05:25&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-07-23T12:12&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-07-16T13:22&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-07-10T09:10&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-07-02T13:25&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-06-22T12:14&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-06-16T10:21&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-06-13T17:33&d=DESC',]

chronic_ukraine_parser_urls_04 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-06-10T13:34&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-06-06T09:40&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-06-02T20:52&d=DESC',
                            'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-05-25T20:27&d=DESC',]
                            
chronic_ukraine_parser_urls_06 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-05-24T16:28&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-05-20T20:03&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-05-16T15:31&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-05-11T16:18&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-05-05T19:00&d=DESC',]
                                
chronic_ukraine_parser_urls_07 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-04-28T14:26&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-04-23T22:28&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-04-17T19:53&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-04-08T14:08&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-04-03T16:20&d=DESC', ]
                                
chronic_ukraine_parser_urls_08 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-03-29T13:09&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-03-21T14:14&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-03-16T13:07&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-03-08T14:41&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-03-02T12:41&d=DESC', ]
                                
chronic_ukraine_parser_urls_09 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-02-23T14:47&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-02-16T17:55&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-02-10T05:43&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-02-04T14:44&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-01-31T03:04&d=DESC', ]
                                
chronic_ukraine_parser_urls_10 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-01-27T12:16&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-01-23T10:14&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-01-18T22:30&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-01-15T14:04&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-01-10T13:10&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-01-05T14:12&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-12-28T11:43&d=DESC', ]
                                
chronic_ukraine_parser_urls_11 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-12-21T16:03&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-12-15T20:15&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-12-10T01:41&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-12-06T14:43&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-11-30T10:26&d=DESC', ]
                                
chronic_ukraine_parser_urls_12 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-11-23T17:40&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-11-18T14:40&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-11-14T14:35&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-11-09T09:16&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-11-03T19:48&d=DESC', ]
                                
chronic_ukraine_parser_urls_13 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-28T17:21&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-24T09:21&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-20T14:32&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-17T15:56&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-11T13:43&d=DESC', ]
                                
                                
chronic_ukraine_parser_urls_14 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-07T17:37&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-05T10:12&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-10-01T16:57&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-29T14:07&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-27T13:31&d=DESC', ]
                                
chronic_ukraine_parser_urls_15 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-24T14:06&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-21T16:22&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-21T09:11&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-19T12:06&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-15T22:20&d=DESC', ]
                                
chronic_ukraine_parser_urls_16 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-13T16:59&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-11T13:48&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-08T17:03&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-09-02T15:37&d=DESC',
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-31T13:05&d=DESC',]
                                
chronic_ukraine_parser_urls_17 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-28T19:52&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-26T06:25&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-23T20:04&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-18T11:46&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-13T17:39&d=DESC', ]
                                
chronic_ukraine_parser_urls_18 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-10T14:52&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-08T12:22&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-08-04T16:17&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-07-29T21:37&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-07-24T12:46&d=DESC',]
                                
chronic_ukraine_parser_urls_19 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-07-19T17:22&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-07-14T19:21&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-07-11T14:09&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-07-07T11:48&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-07-03T12:43&d=DESC', ]
                                
chronic_ukraine_parser_urls_20 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-30T12:32&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-26T10:10&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-21T10:55&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-17T12:19&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-13T17:14&d=DESC', ]

chronic_ukraine_parser_urls_21 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-11T12:23&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-07T13:07&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-05T11:20&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-06-02T15:52&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-31T20:06&d=DESC', ]
                                
chronic_ukraine_parser_urls_22 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-29T09:25&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-26T11:26&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-24T13:13&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-21T11:42&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-19T11:01&d=DESC', ]
                                
chronic_ukraine_parser_urls_23 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-16T20:14&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-13T10:32&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-10T11:09&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-08T03:55&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-05T23:29&d=DESC', ]
                                
chronic_ukraine_parser_urls_24 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-04T13:29&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-05-01T21:40&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-29T16:54&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-26T18:56&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-24T11:34&d=DESC',]
                                
chronic_ukraine_parser_urls_25 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-22T17:09&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-21T00:29&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-19T20:43&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-16T22:24&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-14T16:12&d=DESC', ]
                                
chronic_ukraine_parser_urls_26 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-12T16:15&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-10T10:34&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-08T20:11&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-07T19:56&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-05T13:24&d=DESC', ]
                                
                                
chronic_ukraine_parser_urls_27 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-04T10:26&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-02T14:30&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-04-01T01:19&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-30T05:52&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-29T12:52&d=DESC', ]
                                
chronic_ukraine_parser_urls_28 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-27T12:47&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-26T16:42&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-24T21:42&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-23T22:46&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-22T18:10&d=DESC', ]
                                
chronic_ukraine_parser_urls_29 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-21T02:34&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-19T20:53&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-18T18:45&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-17T13:10&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-16T10:24&d=DESC', ]
                                
chronic_ukraine_parser_urls_30 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-15T03:04&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-14T11:00&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-13T10:08&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-12T05:20&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-11T01:48&d=DESC', ]
                                
chronic_ukraine_parser_urls_31 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-10T02:12&d=DESC',
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-09T03:08&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-08T02:18&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-07T15:01&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-07T02:40&d=DESC', ]
                                
chronic_ukraine_parser_urls_32 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-06T08:33&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-05T16:03&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-04T07:48&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-03T21:11&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-03T12:57&d=DESC', ]
                                
chronic_ukraine_parser_urls_33 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-02T22:44&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-02T09:48&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-01T21:33&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-01T13:40&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-03-01T00:16&d=DESC', ]
                                
chronic_ukraine_parser_urls_34 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-28T18:07&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-28T12:15&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-28T05:09&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-27T21:58&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-27T17:02&d=DESC',]
                                
chronic_ukraine_parser_urls_35 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-27T09:13&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-26T12:36&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-26T05:39&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-25T23:32&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-25T17:29&d=DESC', ]
                                
chronic_ukraine_parser_urls_35 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-25T12:59&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-25T05:25&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T23:26&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T17:08&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T14:27&d=DESC', ]
                                
chronic_ukraine_parser_urls_36 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T12:44&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T10:43&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T09:08&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T07:56&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T06:58&d=DESC', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2022-02-24T06:58&d=DESC', ]

                            
chronic_ukraine_parser_urls_05 = ['https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html', 
                                'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html?a=more&dt=2023-12-17T14:23&d=DESC',]

chronic_palestine_parser_urls_01 = ['https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html',
                                 'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-12-09T22:35&d=DESC',
                                 'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-12-05T14:35&d=DESC',
                                 'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-12-03T05:39&d=DESC',
                                 'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-12-01T05:00&d=DESC',
                                 'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-28T23:47&d=DESC',
                                 'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-26T00:19&d=DESC',
                                 'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-24T08:16&d=DESC',
                                 ]

chronic_palestine_parser_urls_02 = ['https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-22T10:29&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-19T18:23&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-17T13:32&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-15T03:42&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-12T13:45&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-10T04:41&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-07T06:36&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-05T20:08&d=DESC',]

chronic_palestine_parser_urls_03 = ['https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-03T19:31&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-11-02T14:28&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-31T13:25&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-29T10:48&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-27T20:53&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-26T11:08&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-24T12:49&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-23T06:57&d=DESC',]

chronic_palestine_parser_urls_04 = ['https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-21T12:55&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-19T18:43&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-18T15:10&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-17T13:11&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-16T15:48&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-15T19:53&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-14T13:28&d=DESC',
                                    'https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html?a=more&dt=2023-10-13T15:44&d=DESC',]

chronic_parser_urls = ['https://www.interfax.ru/chronicle/obostrenie-palestino-izrailskogo-konflikta.html', 'https://www.interfax.ru/chronicle/voennaya-operacziya-na-ukraine.html', 
                        'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html', 'https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html', 
                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html', 'https://www.interfax.ru/chronicle/putin-pryamaya-liniya-2023.html', 
                        'https://www.interfax.ru/chronicle/ataka-bespilotnikov-na-moskvu.html', 'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html', 
                        'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html', 'https://www.interfax.ru/chronicle/delo-penzenskogo-gubernatora-belozerczeva.html', ]

chronic_karabakh_parser_urls_01 = ['https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html', 
                                'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2023-09-28T09:27&d=DESC',
                                'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2023-09-21T23:19&d=DESC', 
                                'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2023-09-20T17:18&d=DESC', 
                                'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2023-09-20T01:13&d=DESC',]
                                
chronic_karabakh_parser_urls_02 = ['https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2023-09-19T17:04&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2023-09-19T13:21&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2023-01-17T17:16&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2022-09-14T20:48&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2021-07-31T22:56&d=DESC', ]
                                    
chronic_karabakh_parser_urls_03 = ['https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-12-28T10:46&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-11-25T00:32&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-11-17T20:29&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-11-13T09:19&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-11-10T19:27&d=DESC', ]
                                    
chronic_karabakh_parser_urls_04 = ['https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-11-10T02:44&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-11-02T14:05&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-25T21:27&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-18T11:31&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-15T13:07&d=DESC', ]
                                
chronic_karabakh_parser_urls_05 = ['https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-12T14:31&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-10T03:03&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-08T11:26&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-04T20:16&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-03T09:51&d=DESC', ]

chronic_karabakh_parser_urls_06 = ['https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-10-01T17:19&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-09-30T10:09&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-09-29T10:13&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-09-28T07:10&d=DESC', 
                                    'https://www.interfax.ru/chronicle/obostrenie-konflikta-v-nagornom-karabahe.html?a=more&dt=2020-09-27T14:48&d=DESC', ]
                                    

chronic_furgal_parser_urls_01 = ['https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html', 
                                'https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html?a=more&dt=2021-04-07T14:39&d=DESC', 
                                'https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html?a=more&dt=2020-08-31T11:56&d=DESC', 
                                'https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html?a=more&dt=2020-07-20T19:02&d=DESC', 
                                'https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html?a=more&dt=2020-07-15T14:54&d=DESC', ]
                                
chronic_furgal_parser_urls_02 = ['https://www.interfax.ru/chronicle/zaderzhanie-gubernatora-habarovskogo-kraya-sergeya-furgala.html?a=more&dt=2020-07-09T19:17&d=DESC', ]

chronic_school_attack_parser_urls_02 = ['https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2023-08-07T12:05&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2022-09-26T13:13&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2021-12-07T10:13&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2021-09-22T17:21&d=DESC', ]
                                        
chronic_school_attack_parser_urls_03 = ['https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2021-09-20T13:04&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2021-05-20T11:44&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2021-05-11T22:08&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2021-05-11T12:21&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2019-11-14T10:48&d=DESC', ]
                                        
chronic_school_attack_parser_urls_04 = ['https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2018-10-17T15:10&d=DESC', 
                                        'https://www.interfax.ru/chronicle/napadeniya-v-shkolah.html?a=more&dt=2017-09-06T11:18&d=DESC', ]
                                        
chronic_putin_parser_urls_01 = ['https://www.interfax.ru/chronicle/putin-pryamaya-liniya-2023.html', 
                                'https://www.interfax.ru/chronicle/putin-pryamaya-liniya-2023.html?a=more&dt=2023-12-14T14:39&d=DESC', 
                                'https://www.interfax.ru/chronicle/putin-pryamaya-liniya-2023.html?a=more&dt=2023-12-14T12:30&d=DESC', ]
                                
chronic_bespilot_parser_urls_01 = ['https://www.interfax.ru/chronicle/ataka-bespilotnikov-na-moskvu.html', 
                                    'https://www.interfax.ru/chronicle/ataka-bespilotnikov-na-moskvu.html?a=more&dt=2023-08-06T11:58&d=DESC', 
                                    'https://www.interfax.ru/chronicle/ataka-bespilotnikov-na-moskvu.html?a=more&dt=2023-07-24T05:00&d=DESC', ]
                                    
chronic_safonov_parser_urls_01 = ['https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html', 
                                'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html?a=more&dt=2022-03-22T12:07&d=DESC', 
                                'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html?a=more&dt=2021-08-03T11:41&d=DESC', 
                                'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html?a=more&dt=2020-12-10T17:13&d=DESC', 
                                'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html?a=more&dt=2020-08-28T17:30&d=DESC', ]
                                
chronic_safonov_parser_urls_02 = ['https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html?a=more&dt=2020-07-27T22:21&d=DESC', 
                                'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html?a=more&dt=2020-07-08T15:00&d=DESC', 
                                'https://www.interfax.ru/chronicle/delo-protiv-sovetnika-glavy-roskosmosa-ivana-safronova.html?a=more&dt=2020-07-07T10:43&d=DESC', ]
                                
chronic_protiv_parser_urls_01 = ['https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2023-02-02T11:04&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2022-04-21T12:08&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2022-04-05T14:37&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2022-03-23T13:12&d=DESC', ]
                                
chronic_protiv_parser_urls_02 = ['https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2021-08-03T12:44&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2021-05-11T17:13&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2021-04-27T13:29&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2021-04-23T10:20&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2021-04-19T20:28&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2021-04-15T20:54&d=DESC', 
                                'https://www.interfax.ru/chronicle/diplomaticheskoe-protivostoyanie.html?a=more&dt=2021-04-15T20:54&d=DESC',]
                                
chronic_belozer_parser_urls_01 = ['https://www.interfax.ru/chronicle/delo-penzenskogo-gubernatora-belozerczeva.html', 
                                'https://www.interfax.ru/chronicle/delo-penzenskogo-gubernatora-belozerczeva.html?a=more&dt=2021-03-23T11:04&d=DESC', ]


def chronic_news(url):
    resp = requests.get(url)
    news = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        div_list = soup.find_all('div', class_='timeline')
        if div_list:
            for div in div_list:
                chronicle = list(list(url.split('/'))[4].split('.'))[0]
                section_list = div.find_all('section')
                for section in section_list:
                    title = section.find('h3').text
                    created_at = section.find('time')['datetime']
                    href = section.find('a')['href']
                    category = list(href.split('/'))[1]
                    photo = 0
                    if category == '':
                        continue
                    else:
                        if section.find('figure'):
                            figure = section.find('figure')
                            photo = figure.find('img')['src']
                        new_url = 'https://www.interfax.ru/' + href
                        new_resp = requests.get(new_url, headers=headers)
                        text = []
                        if new_resp.status_code == 200:
                            soup = BeautifulSoup(new_resp.content, 'html.parser')
                            div = soup.find('article')
                            if div:
                                p_list = div.find_all('p')
                                for p in p_list:
                                    p = p.text + '& '
                                    text.append(p)
                        description = ''
                        for p in text:
                            description += p
                    news.append({'title': title, 'description': description, 'created_at': created_at,
                                 'photo': photo, 'chronicle_name': chronicle})
                    n += 1
                    time.sleep(4)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 1", n)
    return news
    

def daily_chronic_news(url):
    resp = requests.get(url, headers=headers)
    news = []
    n = 0
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        div_list = soup.find_all('div', class_='timeline')
        if div_list:
            for div in div_list:
                if div.find('time')['datetime'][:10] == str(datetime.date.today()):
                    chronicle = list(list(url.split('/'))[4].split('.'))[0]
                    section_list = div.find_all('section')
                    for section in section_list:
                        title = section.find('h3').text
                        created_at = section.find('time')['datetime']
                        href = section.find('a')['href']
                        category = list(href.split('/'))[1]
                        photo = 0
                        if category == '':
                            continue
                        else:
                            if section.find('figure'):
                                figure = section.find('figure')
                                photo = figure.find('img')['src']
                            new_url = 'https://www.interfax.ru/' + href
                            new_resp = requests.get(new_url, headers=headers)
                            text = []
                            if new_resp.status_code == 200:
                                soup = BeautifulSoup(new_resp.content, 'html.parser')
                                div = soup.find('article')
                                if div:
                                    p_list = div.find_all('p')
                                    for p in p_list:
                                        p = p.text + '& '
                                        text.append(p)
                            description = ''
                            for p in text:
                                description += p
                        news.append({'title': title, 'description': description, 'created_at': created_at,
                                 'photo': photo, 'chronicle_name': chronicle})
                        n += 1
                        time.sleep(4)
        else:
            print('Разметка была изменена')
    else:
        print('Страница не отвечает')
    print("Новости 1", n)
    return news
                            


if __name__ == '__main__':
    file = open('chronicle.json', 'w', encoding='utf-8')
    for url in chronic_ukraine_parser_urls_01:
        news = chronic_news(url)
        file.write(str(news))
    file.close()