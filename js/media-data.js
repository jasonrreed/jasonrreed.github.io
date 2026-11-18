/*
  Media mentions for the Media page and the "Recent commentary" list on the home page.

  To add a new piece, copy one entry and edit it. Order doesn't matter; the site sorts by date.
    type:      "written" (Jason wrote it), "quoted" (interview or quote), "nd" (Notre Dame News), "podcast"
    date:      "YYYY-MM-DD"
    precision: "day" (default), "month" or "year" — how much of the date to show
    described: true when the title is a short description rather than the outlet's headline
    url:       link to the piece; leave it out and the title shows without a link
*/
window.MEDIA = [
  {
    outlet: "The Wall Street Skinny",
    title: "How to Value Anthropic and the AI Trade with Notre Dame’s Professor Jason Reed",
    note: "Podcast interview",
    date: "2026-11-14",
    precision: "month",
    type: "quoted",
    url: "https://podcasts.apple.com/us/podcast/how-to-value-anthropic-and-the-ai-trade-with/id1680425507?i=1000801555749"
  },
  {
    outlet: "International Finance",
    title: "Consumers will bear the burden of new tariffs: Professor Jason Reed",
    note: "Exclusive interview, February 2025 issue",
    date: "2025-02-01",
    precision: "month",
    type: "quoted",
    url: "https://internationalfinance.com/magazine/economy-magazine/consumers-will-bear-the-burden-of-new-tariffs-professor-jason-reed/"
  },
  {
    outlet: "University of Notre Dame",
    title: "Shelter in the Storm",
    note: "Personal essay",
    date: "2020-06-01",
    precision: "year",
    type: "written"
  },
  {
    outlet: "University of Notre Dame",
    title: "I Am Here",
    note: "Feature story",
    date: "2020-06-01",
    precision: "year",
    type: "nd"
  },
  {
    outlet: "Newsweek",
    title: "Trump Approval Rating as Consumer Confidence Drops 70 Days Before Midterm",
    date: "2026-08-27",
    type: "quoted",
    url: "https://www.newsweek.com/trump-approval-rating-as-consumer-confidence-drops-70-days-before-midterm-12365674"
  },
  {
    outlet: "The Conversation",
    title: "Fed struggles to assess state of US economy as government shutdown shuts off key data",
    date: "2025-10-28",
    type: "written",
    url: "https://theconversation.com/fed-struggles-to-assess-state-of-us-economy-as-government-shutdown-shuts-off-key-data-267204"
  },
  {
    outlet: "The Conversation",
    title: "Fed, under pressure to cut rates, tries to balance labor market and inflation – while avoiding dreaded stagflation",
    date: "2025-09-16",
    type: "written",
    url: "https://theconversation.com/fed-under-pressure-to-cut-rates-tries-to-balance-labor-market-and-inflation-while-avoiding-dreaded-stagflation-265361"
  },
  {
    outlet: "Fortune",
    title: "As Harvard’s and Yale’s private equity holdings go on sale, buyers can use this technique for 1,000% windfalls",
    date: "2025-06-15",
    type: "quoted",
    url: "https://fortune.com/2025/06/15/harvard-yale-private-equity-holdings-sale-net-asset-value-discounts-nav-squeezing/"
  },
  {
    outlet: "The Conversation",
    title: "Inflation is heating up again, putting pressure on Trump to cool it on tariffs",
    date: "2025-02-13",
    type: "written",
    url: "https://theconversation.com/inflation-is-heating-up-again-putting-pressure-on-trump-to-cool-it-on-tariffs-249815"
  },
  {
    outlet: "The Conversation",
    title: "Trump’s opening tariff salvo will hurt US consumers − following through on Canada, Mexico threats will increase the price pain",
    date: "2025-02-04",
    type: "written",
    url: "https://theconversation.com/trumps-opening-tariff-salvo-will-hurt-us-consumers-following-through-on-canada-mexico-threats-will-increase-the-price-pain-248991"
  },
  {
    outlet: "The Conversation",
    title: "US inflation rate fell to 2.4% in September − here’s what that means for interest rates and markets",
    date: "2024-10-10",
    type: "written",
    url: "https://theconversation.com/us-inflation-rate-fell-to-2-4-in-september-heres-what-that-means-for-interest-rates-and-markets-240872"
  },
  {
    outlet: "Notre Dame News",
    title: "Notre Dame experts discuss 2022 midterm elections",
    date: "2022-11-03",
    type: "nd",
    url: "https://news.nd.edu/news/notre-dame-experts-discuss-2022-midterm-elections/"
  },
  {
    outlet: "CNN",
    title: "Consumer confidence fell in October as inflation takes a toll",
    date: "2022-10-25",
    type: "quoted",
    url: "https://www.cnn.com/2022/10/25/economy/consumer-confidence-index-october"
  },
  {
    outlet: "CNN",
    title: "Some good inflation news: Wholesale prices fell in August",
    date: "2022-09-14",
    type: "quoted",
    url: "https://edition.cnn.com/2022/09/14/economy/ppi-august-inflation/index.html"
  },
  {
    outlet: "Fox Business",
    title: "US government debt revealed, inflation hotspots and more: Wednesday’s 5 things to know",
    date: "2022-09-14",
    type: "quoted",
    url: "https://www.foxbusiness.com/markets/us-government-debt-revealed-inflation-hotspots-more-wednesdays-5-things-know"
  },
  {
    outlet: "Barron’s",
    title: "Buying Groceries Is Still Painful",
    date: "2022-09-13",
    type: "quoted",
    url: "https://www.barrons.com/livecoverage/stock-market-today-091322/card/buying-groceries-is-still-painful-d2hzy19suEJWpUm2NF5V"
  },
  {
    outlet: "Fox Business",
    title: "Inflation rose faster than expected in August, keeping prices painfully high",
    date: "2022-09-13",
    type: "quoted",
    url: "https://www.foxbusiness.com/economy/inflation-rose-august-prices-gains-slow-remain-near-record-high"
  },
  {
    outlet: "The Wall Street Journal",
    title: "Consumers Lower Their Expectations of Future Inflation",
    date: "2022-08-08",
    type: "quoted",
    url: "https://www.wsj.com/articles/consumers-lower-their-expectations-of-future-inflation-11659993080"
  },
  {
    outlet: "BBC Mundo",
    title: "How the “dumbest theory” can lead you to make wrong financial decisions (and what it has to do with bubbles)",
    date: "2021-02-19",
    type: "quoted",
    note: "In Spanish",
    url: "https://www.bbc.com/mundo/noticias-56099750"
  },
  {
    outlet: "CNBC",
    title: "More bubbles, less shorting. What the GameStop craziness could mean for the future of investing",
    date: "2021-02-06",
    type: "quoted",
    url: "https://www.cnbc.com/2021/02/06/what-the-gamestop-craziness-could-mean-for-the-stock-markets-future.html"
  },
  {
    outlet: "Reuters",
    title: "U.S. employment growth likely rebounded; more government money still needed",
    date: "2021-02-05",
    type: "quoted",
    url: "https://www.reuters.com/article/us-usa-economy/u-s-employment-growth-likely-rebounded-more-government-money-still-needed-idUSKBN2A50EZ"
  },
  {
    outlet: "The Guardian",
    title: "US economy adds 49,000 jobs as Biden aims for further Covid relief",
    date: "2021-02-05",
    type: "quoted",
    url: "https://www.theguardian.com/business/2021/feb/05/us-economy-jobs-biden-covid-relief"
  },
  {
    outlet: "Business Insider",
    title: "S&P 500 and Nasdaq hit records on positive labor-market data",
    date: "2021-02-04",
    type: "quoted",
    url: "https://www.businessinsider.com/stock-market-news-today-indexes-jobless-claims-economic-stimulus-recovery-2021-2"
  },
  {
    outlet: "All Else Equal",
    title: "Co-host, with Forrest Spence, of a podcast that answers student questions with Notre Dame faculty expertise",
    date: "2020-08-01",
    dateLabel: "2020–2022",
    type: "podcast",
    url: "https://podcasts.apple.com/podcast/id1527360041"
  },
  {
    outlet: "Notre Dame News",
    title: "Massive decline in first quarter GDP signals much worse lies ahead, expert says",
    date: "2020-04-29",
    type: "nd",
    url: "https://news.nd.edu/news/massive-decline-in-first-quarter-gdp-signals-much-worse-lies-ahead-expert/"
  },
  {
    outlet: "The Guardian",
    title: "Coverage of the economic toll of record U.S. jobless claims",
    date: "2020-04-16",
    type: "quoted",
    described: true,
    url: "https://www.theguardian.com/business/2020/apr/16/us-unemployment-coronavirus-economic-toll-jobless"
  },
  {
    outlet: "MarketWatch",
    title: "Coverage of whether professional gamblers in Nevada can collect unemployment",
    date: "2020-04-16",
    type: "quoted",
    described: true,
    url: "https://www.marketwatch.com/story/professional-gamblers-in-nevada-may-now-be-able-to-collect-unemployment-2020-04-16"
  },
  {
    outlet: "The Irish Times",
    title: "Coverage of U.S. job losses passing 22 million",
    date: "2020-04-16",
    precision: "month",
    type: "quoted",
    described: true,
    url: "https://www.irishtimes.com/business/economy/more-than-22m-out-of-work-in-us-as-coronavirus-takes-economic-toll-1.4230500"
  },
  {
    outlet: "Yahoo Finance",
    title: "Coverage of Las Vegas gamblers and unemployment benefits",
    date: "2020-04-15",
    precision: "month",
    type: "quoted",
    described: true,
    url: "https://finance.yahoo.com/news/vegas-gamblers-might-qualify-unemployment-155217391.html"
  },
  {
    outlet: "Business Insider",
    title: "Coverage of economists on the surge in jobless claims",
    date: "2020-04-10",
    precision: "month",
    type: "quoted",
    described: true,
    url: "https://www.businessinsider.com/economists-say-jobless-claims-surge-million-weeks-unemployment-insurance-commentary-2020-4"
  },
  {
    outlet: "Fox Business",
    title: "Coverage of record unemployment claims as the pandemic hit the economy",
    date: "2020-03-30",
    precision: "year",
    type: "quoted",
    described: true,
    url: "https://www.foxbusiness.com/economy/us-unemployment-claims-shatter-record-as-coronavirus-hammers-economy"
  },
  {
    outlet: "Notre Dame News",
    title: "Unemployment will get much worse before it gets better, expert says",
    date: "2020-03-26",
    type: "nd",
    url: "https://news.nd.edu/news/unemployment-will-get-much-worse-before-it-gets-better-expert-says/"
  },
  {
    outlet: "CNBC",
    title: "Here’s the only way Trump can win the two-front trade war with China and the EU",
    date: "2018-05-24",
    type: "written",
    url: "https://www.cnbc.com/2018/05/24/trump-trade-wars-with-china-and-eu-pose-growing-global-dangers.html"
  },
  {
    outlet: "CNBC",
    title: "Looming ‘debt hangover’ will crush the economy",
    date: "2018-04-10",
    type: "written",
    note: "Links to Notre Dame’s summary, which links to the op-ed",
    url: "https://mendoza.nd.edu/news/looming-debt-hangover-will-crush-the-economy/"
  },
  {
    outlet: "CNBC",
    title: "China tariffs could be ‘tip of the iceberg’ in a ‘long, entrenched trade war’",
    date: "2018-04-02",
    type: "written",
    url: "https://www.cnbc.com/2018/04/02/china-tariffs-could-be-tip-of-the-iceberg-in-an-entrenched-trade-war.html"
  }
];
