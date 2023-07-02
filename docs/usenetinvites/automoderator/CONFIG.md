    # Auto-reported words/phrases
    title+body: [Rothschild, Scott Kibbey, Data Foundry, usenetreviewz]
    action: spam
    action_reason: Auto-reported words/phrases ({{match-1}})

---

    # Remove Indexers - Indexer owner requested removal
    title+body+url (includes): [doe-hosting, doehosting, doevpn, "oz nzb", oz-nzb, oznzb]
    action: remove
    action_reason: Remove Indexers - Indexer owner requested removal ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed. That indexer's admin/staff have requested removal of all their invite posts. For any questions contact that indexer's admin/staff directly.

---

    # Filter - Comments in specific / sticky / announcement / meta posts
    ## 5bgve2 = /r/UsenetInvites/comments/5bgve2/received_unsolicited_spam_via_pm_recently/
    ## g059mq = https://old.reddit.com/r/UsenetInvites/comments/g059mq/updated_posting_guidelines_aka_how_do_i_post_in/
    type: comment
    parent_submission:
        id: [5bgve2, g059mq]
    priority: 2
    action: filter
    action_reason: Filter - Comments in specific / sticky / announcement / meta posts

---

    ## DISABLED 04/2020
    # Filter - Possible Trading in Consolidated [W] Post
    ## dgnh0w - DOGnzb
    ## 9abkjb, azk0q4, d7kzlz - DrunkenSlug
    ## 7toj20, 9chw70, azk4k3, d7l31r - LuluNZB
    ## 873b5k, 9mcxdl, azk5ez, d7l46h - NZB.Cat
    ## 7xo7r8, 9b4viz, azk3ma, d7l24m - SimplyNZBs
    ## 7xo6lj, 9abo7c, azk2cc, d7l0yj - NZBPlanet
    ## 93h7zy, azk76h, d7l544 - NNZF
    ## type: comment
    ## parent_submission:
        ## id: [7toj20, 7xo6lj, 7xo7r8, 873b5k, 93h7zy, 9abkjb, 9abo7c, 9b4viz, 9chw70, 9mcxdl, azk0q4, azk2cc, azk3ma, azk4k3, azk5ez, azk76h, d7kzlz, d7l0yj, d7l24m, d7l31r, d7l46h, d7l544, dgnh0w]
    ## body (regex): ['\[(H|O)\]', 'can (give|offer|send) .* in return', '(extra|unused) accounts? for', 'have \w+ if interested', 'have .* in return', 'I can (also\W)?invite to', 'I have .* invites?', 'invite from .* for an? invite', 'je peux renvoyer', 'send an? (invitation|invite) back', 'will (\w+)?return the favor']
    ## ~body#whitelist: [can I have a invite, can I have an invite, could I have a invite, could I have an invite, I have read, may I have a invitation, may I have an invitation, may I have a invite, may I have an invite]
    ## priority: 3
    ## action: filter
    ## action_reason: Filter - Possible Trading in Consolidated [W] Post ({{match-body}})

---

    ## DISABLED 04/2020
    # Remove - Wrong invite requests in Consolidated [W] Post
    ## dgnh0w - DOGnzb
    ## 9abkjb, azk0q4, d7kzlz - DrunkenSlug
    ## 7toj20, 9chw70, azk4k3, d7l31r - LuluNZB
    ## 873b5k, 9mcxdl, azk5ez, d7l46h - NZB.Cat
    ## 7xo7r8, 9b4viz, azk3ma, d7l24m - SimplyNZBs
    ## 7xo6lj, 9abo7c, azk2cc, d7l0yj - NZBPlanet
    ## 93h7zy, azk76h, d7l544 - NNZF
    ## type: comment
    ## parent_submission:
        ## id: [7toj20, 7xo6lj, 7xo7r8, 873b5k, 93h7zy, 9abkjb, 9abo7c, 9b4viz, 9chw70, 9mcxdl, azk0q4, azk2cc, azk3ma, azk4k3, azk5ez, azk76h, d7kzlz, d7l0yj, d7l24m, d7l31r, d7l46h, d7l544, dgnh0w]
    ## body (regex): ['looking for (an? invitation|an? invite|invitations|invites) to (dusky|hd.ddict|h.?o.?u|klever|newz.?complex|ng4y|ngforyou|nzb(\.|\W)to|nzb(\.|\W)tv|o.?m.?g|u4a|usenet.?4all)']
    ## priority: 3
    ## action: remove
    ## action_reason: Remove - Wrong invite requests in Consolidated [W] Post ({{match-body}})

---

    # Filter - Users
    ## 5oulKilla - Trolling & attacking /r/Usenet mods
    author: [5oulKilla]
    action: filter
    action_reason: Filter - Users ({{match-author}})

---

    # Shadowban - Users
    ## anon34343433333333, FuzzyKitten95 - Trolling dognzb posts
    ## FickDichDoch2019 - Known invite/account seller https://www.reddit.com/r/usenet/comments/o4fe68/german_movie_usenet_indexer/h2jar7n
    ## jhdscript777 - Repeatedly comments in most every post in the sub
    author: [anon34343433333333, Fat36R, fatterleaf, FickDichDoch2019, FuzzyKitten95, jhdscript777, MagickMouse, MrMcGiver, NOScartio, rowe_foam1, TrendyBiker, VANDARIN, Varvalo, ucrawler]
    action: remove
    action_reason: Shadowban - Users ({{match-author}})

---

    # Remove - Post/Comment overwriting script Link
    body+url (includes): [codepen.io/j0be, pastebin.com/64GuVi2F/12063, greasyfork.org/en/scripts/10380-reddit-overwrite]
    action: remove
    action_reason: Remove - Post/Comment overwriting script Link ({{match-0}})

---

    # Remove - Post/Comment overwriting script Text
    body: ["access the reddit api", "has been overwritten by an open source script to protect"]
    action: remove
    action_reason: Remove - Post/Comment overwriting script Text ({{match-0}})

---

    # Spam - Domains
    ## initiativeq.com - Referral sales/spam
    ## pgblitz.com - Invite threads outside Reddit that break sub rules
    ## robinhood.com/123456 / share.robinhood.com/123456 - Referral sales/spam
    ## Social Ladder / socialladder.rkiapps.com - Referral sales/spam
    ## scriptz-team / newznzb / wtfnzb = nzbx.pw, nzbnewzfrance.ninja, omgwtfnzb.pw, usenet.cat, wtfnzb.pw, .x4b.pw, .x4w.co, xbit.pw
    title+body+url (includes): [crypto.com, dicedreams.com, discord.gg, discordapp.com, guilded.gg, inviteforum.com, inviteland.com, minepi.com, nzbx.pw, minepi.com, nzbnewzfrance, omgwtfnzb.pw, r/everyfuckingthread, r/inviteforum, pgblitz.com, pornfuc.com, robinhood.com, technofrugality.com, telegram.org, temu.com, tiktok.com, torrentinvites.site, trade.re, usenet.cat, usenetreviewz.com, youtu.be, youtube.com, youtube.l.google.com, youtube-nocookie.com, youtubeeducation.com, whatsapp.com, wtfnzb.pw, x4b.pw, x4w.co, xbit.pw]
    priority: 2
    action: spam
    action_reason: Spam - Domains ({{match-1}})

---

    # Spam - Domain short
    ## telegram.org, t.me - Possible invite trading/buying/selling (/r/Invites does not operate a discord channel)
    title+body+url (regex): ['(\b|//)t\.me']
    priority: 2
    action: spam
    action_reason: Spam - Domain short ({{match}})

---

    # Spam - Domains non-domain syntax
    ## initiativeq.com - Referral sales/spam
    ## robinhood.com/123456 / share.robinhood.com/123456 - Referral sales/spam
    ## Social Ladder / socialladder.rkiapps.com - Referral sales/spam
    ## scriptz-team / newznzb / wtfnzb = nzbx.pw, nzbnewzfrance.ninja, omgwtfnzb.pw, usenet.cat, wtfnzb.pw, .x4b.pw, .x4w.co, xbit.pw
    title+body: [everyfuckingthread, initiative q, initiativeq, lemonparty, newznzb, newz nzb, "newz [nzb]", "newz[nzb]", oppfiles, socialladder, social ladder, starkgate, starknet, temu, wtfnzb]
    priority: 2
    action: spam
    action_reason: Spam - Domains non-domain syntax ({{match-1}})

---

    # Spam - Text
    title+body (includes): [airdrop, only fan, onlyfan, teenagers, teens, temu, token]
    priority: 2
    action: spam
    action_reason: Spam - Text ({{match-1}})

---

    # Spam - Newznzb offers - Title
    ## example 1: [O] Own fast nzb index, free api/dl
    ## example 2: [O] NZB Index Site
    ## example 3: [O] NZB Site - 10x invite
    ## example 4: Join unique and fastest NZB site
    ## example 5: [O] Personal nzb site invites
    ## example 6: [O] nEwZ[NZB] - Unique Usenet Site invite
    ## example 7: [O] omgwtfnzbs alternative
    ## example 8: [O] 10x nzb.su and other indexerS
    type: submission
    title (starts-with): ["[O]"]
    title#text (includes): [alternative, and other indexers, Join unique and fastest NZB site, NZB Index Site, NZB Site, Own fast nzb index, Personal nzb site, private indexer, Unique Usenet Site invite]
    priority: 2
    action: spam
    action_reason: Spam - Newznzb offers - Title

---

    # Spam - Newznzb offers - Title - Using fake offers
    ## example 1: [O] dognzb & omgwtfnzbs
    ## example 2: [O] omgwtfnzbs
    ## exampel 3: [O] PFM, DOG, NZBs , OMG invites
    type: submission
    title (full-text): ["[O] dog/omg NZB, town & some other invites", "[O] dognzb & omgwtfnzbs", "[O] omg and dog invites", "[O] omgwtfnzbs", "[O] omgwtfzbs and dognzb", "[O] PFM, DOG, NZBs"]
    author:
        combined_karma: "< 2"
        account_age: < 2
    priority: 2
    action: spam
    action_reason: Spam - Newznzb offers - Title - Using fake offers

---

    # Spam - Newznzb offers - Body
    ## example 1: PM for invite, DO NOT write here!
    ## example 2: newz[NZB] -- Join unique and fastest NZB site
    ## example 3: message me privately for invite
    ## example 4: pm for an invite
    ## example 5: pm to get it :)
    ## example 6: pm me
    ## example 7: PM for it :-))
    type: submission
    title (starts-with): ["[O]"]
    body (includes): [DO NOT write here, message me privately, "newz[NZB]", pm for, pm me, pm to]
    body_shorter_than: 49
    author:
        combined_karma: "< 2"
        account_age: < 2
    priority: 2
    action: spam
    action_reason: Spam - Newznzb offers - Body

---

    # Spam - Newznzb / Scriptz-Team users
    type: any
    author: [2ndgen400, authdev, beefDEADX, BOReX0, cRaNyoNX, dixonkix, eJ8nYwC4NoDc, enzedbee, HPdl160, iNViTeX, inviterxyz, johnlama, kaspertk, KERNEL59, kodezx, konska, kryllia189, momoax, newznab, ohpleaaseee, onomatopoje, pr0mle, rLdEdx, roxxerX, servnix, skyandsand88, tobiasnm, torlama, tuazwxcw, uusenus, wtfnzb, yantarrrr, ZiCE, ZiCEx1, ZiCEx2, ZiCEx3, ZiCEx4, ZiCEx5]
    priority: 2
    action: spam
    action_reason: Spam - Newznzb users

---

   # Spam - Text Comment Spam (Reddit troll/bot)
   type: comment
   body (ends-with): [hello]
   body_longer_than: 6
   author:
       account_age: < 186
   action: spam
   action_reason: Spam - Text Comment Spam (Reddit troll/bot)

---

    # Non Usenet related invite post title blacklist
    type: submission
    title (includes): [32p, 32pag, 32 pag, 52Pojie, "]ar ", " ar ", alpharatio, audionews, bmtv, bitmetv, bcg, bc-g, bitme, blackcat, black cat, btn, broadcast the net, broadcastthe, broadcasthe, brokenstone, cartoon chao, cartoonchao, cg peer, cgpeer, cinemaged, cbt, comicbt, comicsbt, comic bt, comics bt, comic-bt, comics-bt, combicbt, combic bt, demonoid, demoniod, deviloid, exetools, "/extremehorror", freshon, ggn, gazelle, gazzelle, hdbit, hd-bit, hd bit, hound dawg, hounddawg, inmac, ipt, iptorrent, ip torrent, morethan.tv, morethantv, my anonamouse, myanonamouse, myspleen, oneplus, one plus one, "]pth", " pth", "pass the h", passtheh, "]ptp", " ptp", "pass the p", passthep, pornbits, "]phd", " phd", privatehd, raceforme, racingfor, revott, revo tt, scenetime, scene time, smoothstream, sporthd, starstream, stolen app, superchillin, theplace, torrentday, totv, titansof.tv, torrentleech, torrent leech, ttn, transmithe, transmitthe, tvt, tvv, tv vault, tv-vault, ultrahdclub, " wfl", waffles, wcd, what.cd, xrel.to]
    ~title#whitelist (includes): [description, script, subscription]
    set_locked: true
    priority: 1
    action: remove
    action_reason: Non Usenet related invite post title blacklist ({{match-title}})
    comment: |
        Your {{kind}} has been automatically removed. Only usenet related invites are allowed in /r/UsenetInvites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Non Usenet related invite post body/comment blacklist - Tracker
    body (includes): [32p, 32pag, 32 pag, 52Pojie, " ar ", alpharatio, audionews, bmtv, bitmetv, bcg, bc-g, bitme, blackcat, black cat, btn, broadcast the net, broadcastthe, broadcasthe, brokenstone, cartoon chao, cartoonchao, cg peer, cgpeer, cinemaged, cbt, comicbt, comicsbt, comic bt, comics bt, comic-bt, comics-bt, combicbt, combic bt, demonoid, demoniod, deviloid, exetools, "/extremehorror", freshon, ggn, gazelle, gazzelle, hdbit, hd-bit, hd bit, hound dawg, hounddawg, inmac, ipt, iptorrent, ip torrent, morethan.tv, morethantv, my anonamouse, myanonamouse, myspleen, oneplus, one plus one, "]pth", " pth", "pass the h", passtheh, "]ptp", " ptp", "pass the p", passthep, pornbits, "]phd", " phd", privatehd, raceforme, racingfor, revott, revo tt, scenetime, scene time, smoothstream, sporthd, starstream, stolen app, superchillin, theplace, torrentday, totv, titansof.tv, torrentleech, torrent leech, ttn, transmithe, transmitthe, tvt, tvv, tv vault, tv-vault, ultrahdclub, " wfl", waffles, wcd, what.cd, xrel.to]
    body#tail: [invite, invites]
    ~body#whitelist (includes): [description, receipt, script, subscription]
    priority: 1
    action: remove
    action_reason: Non Usenet related invite post title/comment body blacklist - Tracker ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed. Only usenet related invites are allowed in /r/UsenetInvites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Non Usenet related invite post title blacklist - Generic
    # Example 1: "i can offer back an invite to a private movie tracker"
    type: submission
    title: [bittorrent, bittorrent-tracker, pc game site, torrent, torrent-tracker, torrents, tracker, trackers]
    ~title#whitelist: [back from private trackers, convert from torrents, moving from torrents, problems with torrent]
    set_locked: true
    priority: 1
    action: remove
    action_reason: Non Usenet related invite post title blacklist - Generic ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed. Only usenet related invites are allowed in /r/UsenetInvites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Non Usenet related invite post/comment blacklist - Phrase - Generic
    # Example 1: "i can offer back an invite to a private movie tracker"
    body: [bittorrent, bittorrent-tracker, torrent, torrent-tracker, torrents, tracker, trackers]
    body#tail: [invite, invites]
    ~body#whitelist: [back from private trackers, moving from torrents, problems with torrent]
    priority: 1
    action: remove
    action_reason: Non Usenet related invite post/comment blacklist - Phrase - Generic ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed. Only usenet related invites are allowed in /r/UsenetInvites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Non Usenet related invite post body blacklist - Phrase
    # Example 1: "I accept private torrent sites as well."
    type: submission
    body: [accept private torrent]
    set_locked: true
    priority: 1
    action: remove
    action_reason: Non Usenet related invite post body blacklist - Phrase ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed. Only usenet related invites are allowed in /r/UsenetInvites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Locked threads
    parent_submission:
        id: [21ihpe]
    action: remove
    action_reason: Locked threads

---

    # Auto-removed words/domains
    title+body (includes): ["].in", " .in", "*.in", m3.indexone.ch, indexone]
    action: remove
    action_reason: Auto-removed words/domains ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. It contains a blacklisted domain. The owners have opted to not allow discussion of their site here.

---

    # Auto-removed words/domains Regex
    title+body (regex): ['\W?dot\W?\W?in', 'nzbs?\Win', 'nzbs?(\W|\w)?dot(W|\w)?in']
    action: remove
    action_reason: Auto-removed words/domains Regex ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. It contains a blacklisted domain. The owners have opted to not allow discussion of their site here.

---

    # Remove comments and posts promoting trading/selling of invites.
    title+body: [$, amazon gift card, b1tc0in, bitcoin, bitcoins, btc, buy, buying, cash, ether, "échange", exchange, "échanging", exchanging, gift card amazon, l1tc0in, litecoin, litecoins, ltc, mobile pay, mobilepay, moola, payment, paypal, pricing, prices, purchase, purchasing, reciprocal, reciprocate, reciprocation, reciprocity, reddit gold, sale, sell, selling, send me some money, send some coin, send some coins, send you some money, sold, steam wallet, swap, swapsies, tip me, tip you, "T>", trade, trades, trading, usd, visa direct, xchng]
    ~title+body#whitelist: [bitcoin option, bitcoin sign up, bitcoin signup, bitcoins is blank, btc to vip, buy a cert, buy a subscription, buy bitcoin, buy bitcoins, buy btc, buy linden, buy lindens, buy that, buy the vip, buy vip, buying a lifetime, buying a premium, buying a vip, buying vip, cc and bitcoin, comes to bitcoin, end up buying lifetime, feedback in exchange, get into bitcoin, getting into bitcoin, "keep your $", "not drop $10", payment method, use bitcoin, using bitcoin]
    ~title+body#whitelist2 (regex): ['\$\d{1,2} for \d{1,5} api', '\$\d{1,2}\W?(\\|per)\W?(year|yr)', '\$\d{1,2}(year|yr)', 'is spending \$\d{1,2}']
    priority: 3
    action: remove
    action_reason: Remove comments and posts promoting trading/selling of invites. ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove comments and posts promoting trading/selling of invites - Whitelisted
    title+body: [pay, paying]
    ~title+body#whitelist: [a pay site, cheap to pay, pay a registration, pay any invite forward, pay any invites forward, pay attention, pay for 1, pay for 2, pay for a year, pay for one, pay for two, pay for vip, pay or vip, pay forward, pay it back, pay if forward, pay it forward, pay this forward, pay-it-forward, pay more attention, pay my dues, pay them forward, pay this forward, paying forward, paying it forward, paying this forward, unable to pay, unwilling to pay]
    ~title+body#whitelist2 (regex): ['paying.*after.*test(ed|ing)?']
    priority: 3
    action: remove
    action_reason: Remove comments and posts promoting trading/selling of invites - Whitelisted ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove comments and posts promoting trading/selling of invites - Whitelisted
    title+body: [paid]
    ~title+body#whitelist: [paid for, paid indexer, paid indexers, paid one, paid ones, paid plan, paid plans, paid version, paid versions]
    priority: 3
    action: remove
    action_reason: Remove comments and posts promoting trading/selling of invites - Whitelisted ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] posts promoting trading/selling of invites - Title Regex
    type: submission
    title (starts-with): ["[W]"]
    title#2 (regex): ['can send.*((as thanks)|(to you))', 'have .* invites? (left|open) as well', 'I can invite to \w+', 'offering .* invites?']
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [W] posts promoting trading/selling of invites - Title Regex {{match-0}}
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] posts promoting trading/selling of invites - A
    type: submission
    title (starts-with): ["[W]"]
    body: [can invite you, give you something back, I can help you with something, I can offer, I can return the favor, I could return the favor, I could even return the favor, I may be able to help you, I will give you, invite for you, invites for you, return the favor to you, will send an invite to my, will semd an invite to my]
    ~body (regex): ['I can offer upload of (nzb\W?s?)']
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [W] posts promoting trading/selling of invites - A ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] posts promoting trading/selling of invites - B
    type: submission
    title (starts-with): ["[W]"]
    title+body: [", can offer", return the favor]
    ~title+body#whitelist: [could please return the favor, once I have more, for fellow members, return the favor for the next, return the favor on here, someone can return the favor, so I'm here to return, so im here to return, someone could return, to others, to the community, when I eventually have, when I get the chance, when I have them]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [W] posts promoting trading/selling of invites - B ({{match-1}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] posts promoting trading/selling of invites - Phrase A
    ## Example 1: Dognzb invite needed please! Also have 5 nzb.su invites to give away
    ## Example 2: I have some invites for simplynzbs!
    type: submission
    title (starts-with): ["[W]"]
    title+body: [also have, got some, I have]
    title+body#tail: [invite to give, "invites!", invites available if, invites to give, some invites for]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [W] posts promoting trading/selling of invites - Phrase A ({{match-title}}, {{match-title+body}}, {{match-title+body#tail}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] posts promoting trading/selling of invites - Phrase B - Whitelisted
    ## Example 1: "i can offer back an invite"
    ## Example 2: Hi, I'm looking for an pfmonkey.com invite. Can provide nzb.su, dognzb.com or oznzb.com invite in return.
    type: submission
    title (starts-with): ["[W]"]
    body: [can offer, can provide, could offer, I have some, I will give you, in return, my plex]
    body#Tail: [invitation, invite, invites]
    ~body#whitelist: [anyone that can provide a invite, anyone that can provide an invite, anyone who can provide, can offer me, can provide me, indexer that can offer, setting up my plex, someone can offer, someone can provide, someone could offer, they can offer, they could offer, this forum in return, you can provide]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [W] posts promoting trading/selling of invites - Phrase B - Whitelisted ({{match-title}}, {{match-body}}, {{match-body#Tail}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] posts promoting trading/selling of invites - Phrase C
    ## Example 1: "I have 1x WTF that I could provide in return if desired."
    type: submission
    title (starts-with): ["[W]"]
    body: [I have, offer, offering]
    body#Tail: [I could provide, in return]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [W] posts promoting trading/selling of invites - Phrase C ({{match-title}}, {{match-body}}, {{match-body#Tail}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] posts promoting trading/selling of invites - Regex
    type: submission
    title (starts-with): ["[W]"]
    body (regex): ['I have \w+.* (invitations?|invites?)', 'I could give an? \w+.* (invitations?|invites?)', 'I would offer a \w+.* (invitations?|invites?)']
    ~body#whitelist (regex): ['(can|could) I have (a|an) (invitation|invite)', 'I have read the (rules|wiki)']
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [W] posts promoting trading/selling of invites - Regex ({{match-title}}, {{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [W] post comments promoting trading/selling of invites
    type: comment
    parent_submission:
        title (starts-with): ["[W]"]
    body: ["I'll return the favor"]
    parent_submission:
        set_locked: true
    author:
        is_submitter: true
    priority: 3
    action: remove
    action_reason: Remove [W] post comments promoting trading/selling of invites ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [O] posts promoting trading/selling of invites Title
    type: submission
    title (starts-with): ["[O]"]
    title: [I need]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [O] posts promoting trading/selling of invites Title ({{match-0}}, {{match-1}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [O] / [W] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [O] posts promoting trading/selling of invites
    ## Example1: "Also if anyone has an NZB.su invite, I'd appreciate it. Thanks!"
    ## Example2: "And if any of you by any chance has an OMGWTFNZBs I would really appreciate"
    type: submission
    title (starts-with): ["[O]"]
    body: [anyone happen to have, anyone happens to have, anyone has an invite for, I seek, I will gladly accept one, if any of you has, if any of you by any chance has, if any of you have, if any of you by any chance have, if someone could accidentally hit, if someone could hit, "I'm looking for a invite", "I'm looking for an invite", in return, invite if you have one, you just happen to have, you just so happen to have, share against, to give me a]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [O] posts promoting trading/selling of invites ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [O] / [W] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [O] posts promoting trading/selling of invites - Phrase
    type: submission
    title (starts-with): ["[O]"]
    title+body: [also love a invite to, also love an invite to, also searching for, invite for myself, looking for]
    ~title+body#whitelist (regex): ['(any.?body|any.?one) is looking for']
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [O] posts promoting trading/selling of invites - Phrase ({{match-0}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [O] / [W] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove [O] posts promoting trading/selling of invites - Regex
    type: submission
    title (starts-with): ["[O]"]
    title+body (regex): ['(I would|i.?d) (like|love|want) an? (invitation|invite)', '(I would|i.?d) (like|love|want) an? .* (invitation|invite)', '((if anyone (has|have))|(if you have any)|(would appreciate)).*(invitations?|invites?)']
    ~title+body#whitelist: [if you have any questions]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove [O] posts promoting trading/selling of invites - Regex ({{match-0}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [O] / [W] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove trading/selling comments in [W] posts - Phrase
    ## Example 1: I can help with nzb.su, pm me your email. Can you help me with dog?
    type: comment
    body: [can help]
    body#Tail: [can you help]
    parent_submission:
        title (starts-with): ["[W]"]
    priority: 3
    action: remove
    action_reason: Remove trading/selling comments in [W] posts - Phrase
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove trading/selling comments in [W] posts - Regex
    type: comment
    body (regex): ['(a|an|any) (invit|invitation|invite)s? .?please', 'appreciate (a|an) (invit|invitation|invite) to \w+', '(can|could) I have (a|an) (invit|invitation|invite)', 'can (u|you) (perhaps\W)?offer .* (invits?|invitations?|invites?)', '(dm.?d|dmed|messaged|pm.?d|pmed) (for an?|u for an?|you for an?) (invit|invitation|invite)', 'happy to (get|receive) an? (invit|invitation|invite)', 'I please have an? (invit|invitation|invite)', 'I have an? (invit|invitation|invite).*if anyone.*has an? (invit|invitation|invite) for', '(I am|I.?m) looking for \w+', 'I please get (a|an) \w+.* (invit|invitation|invite)', 'I would (like|love) an? (invitation|invite)', 'in return', '(invit|invitation|invite)s? (if you happen to have|if you have (1|one)|if you have more|if you have some more)', '(invit|invite) me', '(invitations?|invites?) (for|with) me', 'looking for \w+.* (invit|invitation|invite|myself)', 'looking for (a|an) (invit|invitation|invite)', '(love|need) an? \w+ (invit|invitation|invite)', '^(love|need) an? (invit|invitation|invite)', '(u|you) have (a|an|any) (invit|invitation|invite)s?']
    ~body#whitelist (regex): ['(can|could) I have (a|an) (invit|invitation|invite) (2|as.?well|too)', 'extra (invitations?|invites?) (for|with) me', 'happy to (get|receive) an? (invit|invitation|invite) (2|as.?well|too)', 'I have (a|an) (invit|invitation|invite)s? .?please', 'I would (like|love) an? (invitation|invite) (2|as.?well|too)', '(invit|invite) me (2|also|as.?well|too)', 'looking for (a|an) (invit|invitation|invite) (2|as.?well|too)', '(u|you) have any', '(u|u are|you|you are) still looking for (a|an) (invit|invitation|invite)', '(u|you) still (love|need) an?']
    parent_submission:
        title (starts-with): ["[W]"]
    author:
        is_submitter: false
    priority: 3
    action: remove
    action_reason: Remove trading/selling comments in [W] posts - Regex ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove trading/selling comments in [W] posts - Regex Submitter
    type: comment
    body (regex): ['I have (a few\W)?(invitations?|invites?)', 'I have an? (invitation|invite).*if anyone.*has an? (invitation|invite) for', 'in return']
    parent_submission:
        title (starts-with): ["[W]"]
    author:
        is_submitter: true
    priority: 3
    action: remove
    action_reason: Remove trading/selling comments in [W] posts - Regex Submitter ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove trading/selling comments in [O] posts - Phrase
    ## Example 1: I can help with nzb.su, pm me your email. Can you help me with dog?
    type: comment
    body: [I also happen to have, will return the favor, would return the favor]
    parent_submission:
        title (starts-with): ["[O]"]
    priority: 3
    action: remove
    action_reason: Remove trading/selling comments in [O] posts - Phrase ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove trading/selling comments in [O] posts - Regex
    ## Example 1: I can help with nzb.su, pm me your email. Can you help me with dog?
    type: comment
    body (regex): ['(any.?body|any.?one) (has|have) (a|an) (invitation|invite)', 'I can also offer .* (invitation|invite)s?', 'I can give you a \w+ (invitation|invite)', 'I can return the favou?r with a \w+ (invitation|invite)', 'I have .* (invitations|invites)', 'I have (1|one)', '(invitations?|invites?) I can send', '(invitations?|invites?|(web)?sites?) that you are after']
    ~body#whitelist (regex): ['(can|could) I have (1|one)', 'I have read the wiki.*(invitations|invites)', 'may I have (1|one)']
    parent_submission:
        title (starts-with): ["[O]"]
    author:
        is_submitter: false
    priority: 3
    action: remove
    action_reason: Remove trading/selling comments in [O] posts - Regex ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove trading/selling comments in [O] posts Submitter
    type: comment
    body (regex): ['happen to have (a\W|an\W)?(invitations?|invites?)', 'I (am in need of|need) (a\W|an\W)?(invitations?|invites?)', 'I can return the favou?r with a \W?\w+.* (invitation|invite)', '(invitations?|invites?) (for|to) .* by (any chance|chance)', '(u|you) have a \W?\w+.* by (any chance|chance)']
    ~body#whitelist: ['I happen to have (a\W|an\W)?(invitations?|invites?)']
    parent_submission:
        title (starts-with): ["[O]"]
    author:
        is_submitter: true
    priority: 3
    action: remove
    action_reason: Remove trading/selling comments in [O] posts Submitter ({{match-body}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow selling or trading of invites. See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove me too comments in [W] posts Regex
    type: comment
    body (regex): ['\[w\]', '\+.?(1|one)', '(1|grateful|I|one) (2|4 me|also|as.?well|for me|too|would 2|would also|would too)', '(2|also|as.?well|too) am looking', 'add me to (that|the) list', '(also|also been) (desperate|desperately|here|interested|looking|need|needed|needing|seeking|use one)', '(also|i.?d|I would) (appreciate|enjoy|like|love) an? \w+?.?(invit|invitation|invite|invitecode)', '(also|could|i.?d|would) (really\W)?(appreciate|like|love|need|use) (1|one)', '(also|i.?d|I would) (be grateful|be happy|want|wanted) to (join|receive|recieve)', 'also if (any.?body|any.?one)', '(any.?body|any.?one|like to) (else has|else have|has|have) (1|an? extra|an? invit|an? invitation|an? invite|an? invitecode|any.?more|invits?|invitations?|invites?|invitecodes?|one)', '(any.?body|any.?one) (has|has any|have|have any|with) (available\W)?(invits|invitations|invites|invitecodes)', '^(any.?more|any others?|more)', '(any.?more|more) (invit|invitation|invite|invitecode)s?', '(any|any.?more|more) (invit|invitation|invite|invitecode|slot)s? (left|remaining)', '(any|any.?more|more) (left|remaining)', 'appreciated?', '(available|spare)\?', '(awesome|help me out|help me out here|interested|looking|love to have it|me|this way) (2|3|also|as.?well|three|too)', '(can|could|may) (I|I please) (also have|have) (1|one)', '(can|could) I (also have|have) (a|an) (invitation|invite|invitecode)', '(can I|could I|trying to) get (1|one)', 'count me in', 'echo', 'extra (invitations?|invites?|invitecodes?) (for|with) me', '(happy|love) to (get|receive|recieve) an? (invit|invitation|invite|invitecode) (2|also|as.?well|too)', '(got|has|have) (a extra|an extra|another|extras|more|one more)', 'help getting (in|into)', '(here|looking|me) also', '(I.?m|I am|I would) (2|also|as.?well|too) (be grateful|be interess?ted|be very interess?ted|interess?ted)', '(I.?d|I.?m|I am|I would) (be grateful|be interess?ted|be very interess?ted|interess?ted)', 'I (need|want) (1|one)', 'I (please\W)?(get|need) (a|an) (invit|invitation|invite|invitecode)', '^(I|I have|I.?ve) read (the wiki|wiki).?$', 'I would (like|love) an? (invitation|invite|invitecode) (2|also|as.?well|too)', 'if (any.?body|any.?one|like to) (has|have)', 'if (op|original poster)', '^(interested|same|samesies)', '(invit|invitation|invite|invitecode) if (any.?body|any.?one) has (1|one)', '(invit|invitation|invite|invitecode) (2|also|as.?well|too)', '(invit|invite) me (2|also|as.?well|too)', '(leech|leeching)', '(looking|this way) (4|for) (a|an) (invit|invitation|invite|invitecode)', '(looking|this way) (4|for) (1|one) of these', '(like|my) (2|also|as.?well|too)', 'me (a|an) (invit|invitation|invite|invitecode)', 'not (just|only) (u|you)', 'or (2|two)', 'piggy.?back', '(same|samesies)($|\W)', 'seconded', 'thanks', 'the feeling', '(throw|toss) my hat', '(u|you) (\&|and) me (2|both|too)', '(u|you) have (a spare|any.?more|any spare|spares?)', '(u|you) still have (1|one)', '(u|you) have (1|one) left', '^(w|want|wanted|wanting)($|\W)', 'with (you|u)', 'yes.? please']
    parent_submission:
        title (starts-with): ["[W]"]
    author:
        is_submitter: false
    priority: 3
    action: remove
    action_reason: Remove me too comments in [W] posts Regex ({{match-body}})

---

    # Remove me too comments in expired [O] posts Regex
    type: comment
    body (regex): ['\[w\]', '\+.?(1|one)', '(1|grateful|I|one) (2|4 me|also|as.?well|for me|too|would 2|would also|would too)', '(2|also|as.?well|too) am looking', 'add me to (that|the) list', '(also|also been) (desperate|desperately|here|interested|looking|need|needed|needing|seeking|use one)', '(also|i.?d|I would) (appreciate|enjoy|like|love) an? \w+?.?(invit|invitation|invite|invitecode)', '(also|could|i.?d|would) (really\W)?(appreciate|like|love|need|use) (1|one)', '(also|i.?d|I would) (be grateful|be happy|want|wanted) to (join|receive|recieve)', 'also if (any.?body|any.?one)', '(any.?body|any.?one|like to) (else has|else have|has|have) (1|an? extra|an? invit|an? invitation|an? invite|an? invitecode|any.?more|invits?|invitations?|invites?|invitecodes?|one)', '(any.?body|any.?one) (has|has any|have|have any|with) (available\W)?(invits|invitations|invites|invitecodes)', '^(any.?more|any others?|more)', '(any.?more|more) (invit|invitation|invite|invitecode)s?', '(any|any.?more|more) (invit|invitation|invite|invitecode|slot)s? (left|remaining)', '(any|any.?more|more) (left|remaining)', 'appreciated?', '(available|spare)\?', '(awesome|help me out|help me out here|interested|looking|love to have it|me|this way) (2|3|also|as.?well|three|too)', '(can|could|may) (I|I please) (also have|have) (1|one)', '(can|could) I (also have|have) (a|an) (invitation|invite|invitecode)', '(can I|could I|trying to) get (1|one)', 'count me in', 'echo', 'extra (invitations?|invites?|invitecodes?) (for|with) me', 'happy to (get|receive|recieve) an? (invit|invitation|invite|invitecode) (2|also|as.?well|too)', '(got|has|have) (a extra|an extra|another|extras|more|one more)', 'help getting (in|into)', '(here|looking|me) also', '(I.?m|I am|I would) (2|also|as.?well|too) (be grateful|be interess?ted|be very interess?ted|interess?ted)', '(I.?d|I.?m|I am|I would) (be grateful|be interess?ted|be very interess?ted|interess?ted)', 'I (need|want) (1|one)', 'I (please\W)?(get|need) (a|an) (invit|invitation|invite|invitecode)', '^(I|I have|I.?ve) read (the wiki|wiki).?$', 'I would (like|love) an? (invitation|invite|invitecode) (2|also|as.?well|too)', 'if (any.?body|any.?one|like to) (has|have)', 'if (op|original poster)', '^(interested|same|samesies)', '(invit|invitation|invite|invitecode) if (any.?body|any.?one) has (1|one)', '(invit|invitation|invite|invitecode) (2|also|as.?well|too)', '(invit|invite) me (2|also|as.?well|too)', '(leech|leeching)', '(looking|this way) (4|for) (a|an) (invit|invitation|invite|invitecode)', '(looking|this way) (4|for) (1|one) of these', '(like|my) (2|also|as.?well|too)', 'me (a|an) (invit|invitation|invite|invitecode)', 'not (just|only) (u|you)', 'or (2|two)', 'piggy.?back', '(same|samesies)($|\W)', 'seconded', 'thanks', 'the feeling', '(throw|toss) my hat', '(u|you) (\&|and) me (2|both|too)', '(u|you) have (a spare|any.?more|any spare|spares?)', '(u|you) still have (1|one)', '(u|you) have (1|one) left', '^(w|want|wanted|wanting)($|\W)', 'with (you|u)', 'yes.? please']
    parent_submission:
        title (starts-with): ["[O]"]
        flair_text: ["NO MORE INVITES"]
    priority: 3
    action: remove
    action_reason: Remove me too comments in expired [O] posts Regex ({{match-body}})

---

    # Remove me too comments in expired [O] posts Specific
    ## Same body as flair [W] rule
    type: comment
    ~body: [all good, all okay, all set, "all set, thanks!", all sorted, am good, am set, completed, done, "done.", found one, filled, fulfilled, good to go, "good to go.", "good to go!", "good to go,", "Good to go :)", got a code, got a invite, got an invitation, got an invite, got invite, got it, got mine, got my invite, got one, got the invite, got the invites, got what I wanted, got your invitation, got your invite, gtg, has the invite, have the invite, hooked me up, hooked up, I got, I have one, I was offered a invite, I was offered an invite, Im good, "I'm good", invite received, "invite received!", "Invite received. Thanks!", invited, kind to give me a invite, kind to give me an invite, no invite needed, no longer needed, please close, post is closed, received, recieved, "received an invite!", "received invite.", "received one. good to go thanks!", sent a invite, sent an invite, served to me, signed up, sorted, squared, taken care of, thank you, "that's all"]
    parent_submission:
        title (starts-with): ["[O]"]
        flair_text: ["NO MORE INVITES"]
    author:
        is_submitter: false
    priority: 3
    action: remove
    action_reason: Remove me too comments in expired [O] posts Specific

---

    # Remove comments and lock expired [W] posts
    type: comment
    parent_submission:
        title (starts-with): ["[W]"]
        flair_text: ["NO MORE INVITES"]
        set_locked: true
    author:
        is_submitter: false
    priority: 3
    action: remove
    action_reason: Remove comments and lock expired [W] posts

---

    ## DISABLED 04/2020
    # Remove [W] posts that do not acknowledge reading the starting out wiki (rule 5)
    ## type: submission
    ## title: ["[W]"]
    ## ~title+body (includes): [startingout, wiki]
    ## action: remove
    ## action_reason: Remove [W] posts that do not acknowledge reading the starting out wiki (rule 5)
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites per rule #5. Please read https://www.reddit.com/r/UsenetInvites/wiki/startingout before creating a [W] post.

---

    # Remove suspect vote manipulation
    type: submission
    body: [upvote my post, upvote the post, upvote this post]
    set_locked: true
    priority: 1
    action: remove
    action_reason: Remove suspect vote manipulation {{match-body}}
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. Please refrain from asking for votes, upvotes, etc. since that will break Reddit.com vote manipulation rules https://www.reddithelp.com/hc/en-us/articles/360043066412

---

    # Remove blank/empty [O]/[W] post titles
    type: submission
    title (full-text): ["[W]", "[O]"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 1
    action: remove
    action_reason: Remove blank/empty [O]/[W] post titles
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. Please include more information in your post title describing what type of invite you are offering or want.

---

    ## Remove all posts by untrusted karma whore accounts
    type: submission
    author:
        flair_text: [badkarma]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove all posts by untrusted karma whore accounts
    comment: |
        Your post has been removed. Reddit users submitting any posts must have prior Reddit history

        * Must be 3+ months old and have 30+ comment karma
        * Reddit history and karma must be real e.g. participation in karma building subs or spam rings will disqualify you from submitting posts and receiving flair.

        See https://www.reddit.com/r/UsenetInvites/wiki/postinguidelines

---

    ## Remove Offering posts without valid comment karma
    type: submission
    title (starts-with): ["[O]"]
    author:
        comment_karma: "< 30"
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove Offering posts without valid comment karma
    comment: |
        Your post has been removed. Reddit users submitting [O] posts must have prior Reddit history (Must be 3+ months old and have 30+ comment karma).

        See https://www.reddit.com/r/UsenetInvites/wiki/postinguidelines

---

    ## Remove Offering posts without valid account age
    type: submission
    title (starts-with): ["[O]"]
    author:
        account_age: < 90
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove Offering posts without valid account age
    comment: |
        Your post has been removed. Reddit users submitting [O] posts must have prior Reddit history (Must be 3+ months old and have 30+ comment karma).

        See https://www.reddit.com/r/UsenetInvites/wiki/postinguidelines

---

    ## Remove Comments in non-verified [O] posts by untrusted karma whore accounts
    type: comment
    parent_submission:
        title (starts-with): ["[O]"]
        flair_text: ["OFFERING", "NO MORE INVITES"]
    author:
        flair_text: [badkarma]
    priority: 2
    action: remove
    action_reason: Remove Comments in non-verified [O] posts by untrusted karma whore accounts

---

    ## Remove Comments in non-verified [O] posts without valid comment karma
    type: comment
    parent_submission:
        title (starts-with): ["[O]"]
        flair_text: ["OFFERING", "NO MORE INVITES"]
    author:
        comment_karma: "< 30"
    priority: 2
    action: remove
    action_reason: Remove Comments in non-verified [O] posts without valid comment karma

---

    ## Remove Comments in non-verified [O] posts without valid account age
    type: comment
    parent_submission:
        title (starts-with): ["[O]"]
        flair_text: ["OFFERING", "NO MORE INVITES"]
    author:
        account_age: < 90
    priority: 2
    action: remove
    action_reason: Remove Comments in non-verified [O] posts without valid account age

---

    ## Remove Wanted posts without valid user flair
    type: submission
    title (starts-with): ["[W]"]
    author:
        ~flair_text: [verified]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove Wanted posts without valid user flair
    comment: |
        Your post has been removed. Reddit users submitting [W] posts must have "verified" user flair - This is obtained by Offering invites first.

        See https://www.reddit.com/r/UsenetInvites/wiki/postinguidelines

---

    ## DISABLED 04/2020
    # Remove posts requesting indexers in their own [W] consolidated post - DOGnzb
    ## title (starts-with): ["[W]", "[O]"]
    ## title#Indexer (includes): [dog, woof]
    ## priority: 2
    ## action: remove
    ## action_reason: Remove posts requesting indexers in their own [W] consolidated post - DOGnzb
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites. Please use the consolidated post for DOGnzb invites.
        ##
        ## https://www.reddit.com/r/UsenetInvites/comments/dgnh0w/w_consolidated_dognzb/

---

    ## DISABLED 04/2020
    # Remove posts requesting indexers in their own [W] consolidated post - DrunkenSlug
    ## title (starts-with): ["[W]", "[O]"]
    ## title#Indexer (includes): [drunken, inebriated nzb co, inebriated nzbco, inebriatednzbco, inebriatedslug, slug]
    ## priority: 2
    ## action: remove
    ## action_reason: Remove posts requesting indexers in their own [W] consolidated post - DrunkenSlug
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites. Please use the consolidated post for DrunkenSlug invites.
        ##
        ## https://www.reddit.com/r/UsenetInvites/comments/d7kzlz/w_consolidated_drunkenslug/

---

    # Remove posts requesting indexers in their own [W] consolidated post - LuluNZB
    ## title (starts-with): ["[W]", "[O]"]
    ## title#Indexer (includes): ["]lulu", " lulu"]
    ## priority: 2
    ## action: remove
    ## action_reason: Remove posts requesting indexers in their own [W] consolidated post - LuluNZB
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites. Please use the consolidated post for LuluNZB invites.
        ##
        ## https://www.reddit.com/r/UsenetInvites/comments/d7l31r/w_consolidated_lulunzb/

---

    ## DISABLED 04/2020
    # Remove posts requesting indexers in their own [W] consolidated post - NNZF.io
    ## title (starts-with): ["[W]", "[O]"]
    ## title#Indexer (includes): [nnzf, nnfz, nzf, nfz]
    ## priority: 2
    ## action: remove
    ## action_reason: Remove posts requesting indexers in their own [W] consolidated post - NNZF.io
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites. Please use the consolidated post for NNZF.io invites.
        ##
        ## https://www.reddit.com/r/UsenetInvites/comments/d7l544/w_consolidated_nnzf/

---

    ## DISABLED 04/2020
    # Remove posts requesting indexers in their own [W] consolidated post - NZB.Cat
    ## title (starts-with): ["[W]", "[O]"]
    ## title#Indexer (includes): [cat]
    ## priority: 2
    ## action: remove
    ## action_reason: Remove posts requesting indexers in their own [W] consolidated post - NZB.Cat
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites. Please use the consolidated post for NZB.Cat invites.
        ##
        ## https://www.reddit.com/r/UsenetInvites/comments/d7l46h/w_consolidated_nzbcat/

---

    ## DISABLED 04/2020
    # Remove posts requesting indexers in their own [W] consolidated post - NZBPlanet
    ## title (starts-with): ["[W]", "[O]"]
    ## title#Indexer (includes): ["]nzbpla", "]planet", " nzbpla", " planet"]
    ## priority: 2
    ## action: remove
    ## action_reason: Remove posts requesting indexers in their own [W] consolidated post - NZBPlanet
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites. Please use the consolidated post for NZBPlanet invites.
        ##
        ## https://www.reddit.com/r/UsenetInvites/comments/d7l0yj/w_consolidated_nzbplanet/

---

    ## DISABLED 04/2020
    # Remove posts requesting indexers in their own [W] consolidated post - SimplyNZBs
    ## title (starts-with): ["[W]", "[O]"]
    ## title#Indexer (includes): ["]simply", " simply"]
    ## priority: 2
    ## action: remove
    ## action_reason: Remove posts requesting indexers in their own [W] consolidated post - SimplyNZBs
    ## comment: |
        ## Your {{kind}} has been automatically removed from /r/UsenetInvites. Please use the consolidated post for SimplyNZBs invites.
        ##
        ## https://www.reddit.com/r/UsenetInvites/comments/d7l24m/w_consolidated_simplynzbs/

---

    # Filter suspected rule broken
    type: submission
    title+body: [unnameable, unnameables, unmentionable, unmentionables]
    priority: 2
    action: filter
    action_reason: Filter suspected rule broken ({{match-0}})

---

    # Filter suspected trading in a [O] post
    type: submission
    title (starts-with): ["[O]"]
    body: [big ask]
    priority: 2
    action: filter
    action_reason: Filter suspected trading in a [O] post

---

    # Filter suspected [W] comments in a [W] post
    type: comment
    body: [can I have a invite, can I have an invite, invite please, like to get, love to get, take a invite, take an invite, yes please, you still have]
    author:
        is_submitter: false
    parent_submission:
        title (starts-with): ["[W]"]
    priority: 2
    action: filter
    action_reason: Filter suspected [W] comments in a [W] post

---

    # Filter too many [W] posts by certain users, manual approval required
    ## not active yet
    ##
    # type: submission
    # title (starts-with): ["[W]"]
    # author: []
    # priority: 3
    # action: filter
    # action_reason: Filter too many [W] posts by certain users, manual approval required

---

    # Filter vague posts requesting invites that may not exist - german
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer: [for you know who, german, germany]
    priority: 2
    action: filter
    action_reason: Filter vague posts requesting invites that may not exist - german

---

    ## Disabled Rule 03/15/2018, looks like DOGnzb re-enabled invites
    ##
    # Remove posts requesting indexers without invites - DOGnzb
    # title (starts-with): ["[W]"]
    # title#Indexer (includes): [dog]
    # action: remove
    # action_reason: Remove posts requesting indexers without invites - DOGnzb
    # comment: |
        # Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no DOGnzb invites available. Feel free to chat with staff on their IRC channel for any updated info ([synIRC irc.synirc.net](https://www.synirc.net/), join #dognzb).

        # Alternatively, try https://dognzb.cr/register to check if they currently have open registration.

---

    # Remove posts requesting indexers without invites - HDAddicts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [hd addict, hdaddict, "hd@ddict"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - HDAddicts
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no HDAddicts invites available. Feel free to talk to their staff/administrators for any updated info.

        Alternatively, try [their website](http://www.hdaddicts.net/Forums/index.php?app=core&module=global&section=register) to check if they currently have open registration.

---

    # Remove posts requesting indexers without invites - House-Of-Usenet
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): ["]hou", " hou", "h o u", "h-o-u"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - House-Of-Usenet
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no House-Of-Usenet invites available. Feel free to talk to their staff/administrators for any updated info.

---

    # Remove posts requesting indexers without invites - Kleverig
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [klever]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - Kleverig
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no Kleverig invites available. Feel free to talk to their staff/administrators for any updated info.

---

    # Remove posts requesting/offering indexers without invites - BD25
    type: submission
    title#Indexer (includes): [bd25]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting/offering indexers without invites - BD25
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no BD25 invites available. Feel free to talk to their staff/administrators for any updated info.

        Alternatively, try [their website here](bd25.eu/smf) or [their website here](http://www.bd25.eu/index.php?page=signup) to check if they currently have open registration.

---

    # Remove posts requesting/offering indexers without invites - LuluNZB
    ## LuluNZB has a broken/unusable invite system, members unable to send invites https://www.reddit.com/r/UsenetInvites/comments/hkqhhy/o_5_x_lulunzb/
    type: submission
    title#Indexer (includes): [lulu]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting/offering indexers without invites - LuluNZB
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no LuluNZB invites available. Feel free to talk to their staff/administrators for any updated info.

        Alternatively, try [their website](https://lulunzb.com/register) to check if they currently have open registration.

---

    # Remove posts requesting indexers without invites - newz-complex
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [complex]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - newz-complex
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no newz-complex invites available. Feel free to talk to their staff/administrators for any updated info.

---

    # Remove posts requesting indexers without invites - NG4You (unconfirmed)
    ## Added 03/25/2018 - No invites have been offered in past 30+ days
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [ng4y, ngforyou]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - NG4You (unconfirmed)
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no NG4You invites available. Feel free to talk to their staff/administrators for any updated info.

        Alternatively, try http://www.ng4you.com/?inscription to check if they currently have open registration.

---

    # Remove posts requesting indexers without invites - nzb.to
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): ["nzb.to", "nzb .to"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - nzb.to
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no nzb.to invites available. Feel free to talk to their staff/administrators for any updated info.

---

    # Remove posts requesting indexers without invites - nzb.tv (unconfirmed)
    ## Added 03/25/2018 - No invites have been offered in past 30+ days
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): ["nzb.tv", "nzb .tv", nzbtv]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - nzb.tv (unconfirmed)
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no nzb.tv invites available. Feel free to talk to their staff/administrators for any updated info.

        Alternatively, try https://nzb.tv/register to check if they currently have open registration.

---

    # Remove posts requesting indexers without invites - nzb-sa
    ## Added 12/2020 - Invite system disabled https://www.reddit.com/r/UsenetInvites/comments/k44q9f/w_nzbsa/gecvauq/
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [nzb-sa, " nzbsa"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - nzb-sa
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no nzb-sa invites available. Feel free to talk to their staff/administrators for any updated info.

        Alternatively, try https://nzbsa.co.za/register to check if they currently have open registration.

---

    ## Last invite windows 02/27/2023 - 03/06/2023, 10/09/2022 - 10/20/2022
    # Remove posts requesting indexers without invites - omgwtfnzbs
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): ["omfgwtf", "omfwtf", "omg", "o.m.g", "0mg", "o m g", "oh em", "oh em", "oh m", "ohem g", "ohemg"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - omgwtfnzbs
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no omgwtfnzbs invites available. Feel free to chat with staff on their IRC channel for any updated info ([synIRC](https://www.synirc.net/servers), join #omgwtfnzbs.support).

        Alternatively, try https://omgwtfnzbs.me/new-vip to check if they currently have open registration.

---

    ## Last invite windows 02/27/2023 - 03/06/2023, 10/09/2022 - 10/20/2022
    # Remove posts requesting indexers without invites - omgwtfnzbs
    type: submission
    title (starts-with): ["[W]"]
    body (includes): ["omfgwtf", "omfwtf", "omg", "o.m.g", "0mg", "o m g", "oh em", "oh em", "oh m", "ohem g", "ohemg"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - omgwtfnzbs
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no omgwtfnzbs invites available. Feel free to chat with staff on their IRC channel for any updated info ([synIRC](https://www.synirc.net/servers), join #omgwtfnzbs.support).

        Alternatively, try https://omgwtfnzbs.me/new-vip to check if they currently have open registration.

---

    # Remove posts requesting indexers without invites - unfr formerly nnzf
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): ["]nnzf", "]unfr", "] nnzf", "] unfr", "nnzf.io", "unfr.pw"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - unfr formerly nnzf
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no unfr.pw invites available. Feel free to talk to their staff/administrators for any updated info.

---

    # Remove posts requesting indexers without invites - U4A (Usenet-4all)
    ## https://www.reddit.com/r/UsenetInvites/comments/8zsoqq/w_usenet4all/e2lt24j
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [4 all, "4-all", 4all, u4a]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - U4A (Usenet-4all)
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no Usenet-4all invites available. Feel free to talk to their staff/administrators for any updated info.

        Alternatively, try https://usenet-4all.pw/forum/register.php to check if they currently have open registration.

---

    # Remove posts requesting indexers without invites - usenet-space-cowboys.online
    ## https://www.reddit.com/r/UsenetInvites/comments/8zzmhx/w_usenetspacecowboysonline_invite/e2mtefx
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [cowboy]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - usenet-space-cowboys.online
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no usenet-space-cowboys invites available. Feel free to talk to their staff/administrators for any updated info.

---

    # Remove posts requesting indexers without invites - Wizznab
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [wiznab, wizznab]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts requesting indexers without invites - Wizznab
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. There are currently no Wizznab invites available. Wizznab no longer exists.

        See https://www.reddit.com/r/usenet/comments/7bsitd/wizznabtk_down/

---

    ## Disabled Rule 03/15/2018, looks like DOGnzb re-enabled invites
    ##
    # Remove posts offering indexers without invites, fake offer
    ## Author Whitelist: batcow, dogzipp, nfodiz = DOGnzb staff
    # title (starts-with): ["[O]"]
    # title#Indexer (includes): [dog]
    # ~title#whitelist: [open for new registrations, open for registration, open registration, open signup, registration is currently open, registration open, registrations are open]
    # ~author: [batcow, dogzipp, nfodiz]
    # priority: 2
    # action: spam
    # action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [bd25]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    # ~author: []
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [hd addict, hdaddict, "hd@ddict"]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    # ~author: []
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): ["]hou", " hou", "h o u", "h-o-u"]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    # ~author: []
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [klever]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    # ~author: []
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [complex]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    # ~author: []
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [nzb.to, "nzb .to"]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    # ~author: []
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    ## Last invite windows 02/27/2023 - 03/06/2023, 10/09/2022 - 10/20/2022
    # Remove posts offering indexers without invites, fake offer
    ## Author Whitelist: omgstaff = omgwtfnzbs staff
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [omg]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    ~author: [omgstaff]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): ["]nnzf", "]unfr", "] nnzf", "] unfr", "nnzf.io", "unfr.pw"]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [4 all, "4-all", 4all, u4a]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, fake offer
    ## https://www.reddit.com/r/UsenetInvites/comments/8zzmhx/w_usenetspacecowboysonline_invite/e2mtefx
    type: submission
    title (starts-with): ["[O]"]
    title#Indexer (includes): [cowboy]
    ~title#whitelist: [open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: spam
    action_reason: Remove posts offering indexers without invites, fake offer

---

    # Remove posts offering indexers without invites, open signup
    type: submission
    title: [open day, open for new registrations, open for registration, open invitation, open invitations, open invite, open invites, open registration, open signup, registration is currently open, registration is open, registration open, registrations are open]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 2
    action: remove
    action_reason: Remove posts offering indexers without invites, open signup

---

    # Remove posts offering indexers without quantity Title
    ## Author Whitelist: beerforbrains = abook.ws; bent01 = nzbfinder.ws; lulunzb = lulunzb
    type: submission
    title (starts-with): ["[O]"]
    ~title#Quantity (regex): ['(\d{1,2}|\d{1,2}x|x\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen)']
    ~title#whitelistkeywords: [open, registration]
    ~author: [beerforbrains, bent01, lulunzb]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    action: remove
    action_reason: Remove posts offering indexers without quantity Title
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. Your post title must include the number of invites you are offering.
        For example: "[O] 2 invites to Awesome-Indexer-Name"

---

    ## DISABLED 04/16/2020 POSSIBLY DELETE LATER
    # Filter remove posts offering invites without quantity, possible fake offer
    ## Author Whitelist: beerforbrains = abook.ws; bent01 = nzbfinder.ws; lulunzb = lulunzb
    # title (starts-with): ["[O]"]
    # ~title#Quantity (includes,regex): ['\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|couple|several']
    # ~title#whitelistkeywords: [open, registration]
    # ~body (regex): ['\d{1,2}.*(available|invites)', '(first|got|have|maybe)\W(\d{1,2}|one|two|three|four|five|fifteen)', '(some|several)\Winvites']
    # ~author: [beerforbrains, bent01, lulunzb]
    # action: filter
    # action_reason: Filter remove posts offering invites without quantity, possible fake offer

---

    # Remove unknown/vague invite requests title
    type: submission
    title (starts-with): ["[W]"]
    title (regex): ['anything']
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    action: remove
    action_reason: Remove unknown/vague invite requests title ({{match-body}})

---

    # Remove unknown/vague invite requests body
    type: submission
    title (starts-with): ["[W]"]
    body (regex): ['indexers if you know', 'interested in any.*indexers']
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    action: remove
    action_reason: Remove unknown/vague invite requests body ({{match-body}})

---

    # Filter unknown/vague invite requests - whitelisting known indexers
    type: submission
    title (starts-with): ["[W]"]
    ~title#whitelist (includes): [4all, 6box, abook, althub, bd25, brother of usenet, brothers of usenet, brother-of-usenet, brothers-of-usenet, cat, chica, dobnzb, dog, " ds", drunken, drunkenslag, slug, dusky, fastnzb, finder, geek, gingadaddy, hangout, hellafast, hduse, indiausenet, pfm, monkey, lulnzb, lulu, mcm, "media center master", miatrix, mooty, newseros, newshost, newz-complex, newztown, ng4you, ninja central, ninjacentral, nmatrix, nnzf, nzb.ag, nzb.dan.tm, nzb.io, nzb.to, nzb-sa, nzbsa.co.za, nzb.su, nzb.tv, nzbcave, planet nzb, planetnzb, nbz planet, nzb planet, nbzplanet, nzbplanet, nzbquality, nzbs.io, nzbs.org, nzbs.today, nzbtv, omgwtfnzb, piratenzb, samuraiplace, simplynbz, simplynzb, "sky-of-use.net", sky of usenet, skyofusenet, sooti, tabula, town, unfr, u4a, usenet4all, usenet-space-cowboys, usenethd, underground-of-hd, wombles]
    action: filter
    action_reason: Filter unknown/vague invite requests - whitelisting known indexers

---

    # Filter unknown/vague invite offers - whitelisting known indexers
    type: submission
    title (starts-with): ["[O]"]
    ~title#whitelist (includes): [4all, 6box, abook, althub, bd25, brother of usenet, brothers of usenet, brother-of-usenet, brothers-of-usenet, cat, chica, dobnzb, dog, " ds", drunken, drunkenslag, slug, dusky, fastnzb, finder, geek, gingadaddy, hangout, hellafast, hduse, indiausenet, pfm, monkey, lulnzb, lulu, mcm, "media center master", miatrix, mooty, newseros, newshost, newz-complex, newztown, ng4you, ninja central, ninjacentral, nmatrix, nnzf, nzb.ag, nzb.dan.tm, nzb.io, nzb-sa, nzbsa.co.za, nzb.su, nzb.to, nzb.tv, nzbcave, planet nzb, planetnzb, nbz planet, nzb planet, nbzplanet, nzbplanet, nzbquality, nzbs.io, nzbs.org, nzbs.today, nzbtv, omgwtfnzb, piratenzb, samuraiplace, simplynbz, simplynzb, "sky-of-use.net", sky of usenet, skyofusenet, sooti, tabula, town, u4a, usenet4all, usenet-space-cowboys, usenethd, underground-of-hd, wombles]
    action: filter
    report_reason: This [O] {{kind}} seems to be offering an invite to an unknown indexer, please review.

---

    # Remove unknown/vague invite offers (w/ threshold checks) - whitelisting known indexers
    type: submission
    title (starts-with): ["[O]"]
    ~title#whitelist (includes): [4all, 6box, abook, althub, bd25, brother of usenet, brothers of usenet, brother-of-usenet, brothers-of-usenet, cat, chica, dobnzb, dog, " ds", drunken, drunkenslag, slug, dusky, fastnzb, finder, geek, gingadaddy, hangout, hellafast, hduse, indiausenet, pfm, monkey, lulnzb, lulu, mcm, "media center master", miatrix, mooty, newseros, newshost, newz-complex, newztown, ng4you, ninja central, ninjacentral, nmatrix, nnzf, nzb.ag, nzb.dan.tm, nzb.io, nzb-sa, nzbsa.co.za, nzb.su, nzb.to, nzb.tv, nzbcave, omgwtfnzb, planet nzb, planetnzb, nbz planet, nzb planet, nbzplanet, nzbplanet, nzbquality, nzbs.io, nzbs.org, nzbs.today, nzbtv, omg, piratenzb, samuraiplace, simplynbz, simplynzb, "sky-of-use.net", sky of usenet, skyofusenet, sooti, tabula, town, u4a, usenet4all, usenet-space-cowboys, usenethd, underground-of-hd, wombles]
    author:
        combined_karma: "< 2"
        account_age: < 2
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    action: remove
    action_reason: Remove unknown/vague invite offers (w/ threshold checks) - whitelisting known indexers
    modmail: This {{kind}} by /u/{{author}} has been removed due to an unrecognized indexer invite being offered by a new-ish Reddit account. Please investigate.

---

    # Send an alert to modmail if anything gets 2+ reports
    #reports: 2
    #modmail: The above item has received 2+ reports, please investigate.

---

    # Automatically remove anything that gets 2+ reports and send modmail
    reports: 2
    action: remove
    action_reason: Automatically remove anything that gets 2+ reports and send modmail
    modmail: The above item was automatically removed due to receiving 2+ reports. Please verify that this action was correct.

---

    # Required tags
    type: submission
    ~title (starts-with): ["[W]", "[O]"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    action: remove
    action_reason: Required tags
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites because the title does not include proper title tags.

        If you are wanting an invite, please start your post with [W].  If you have invites to offer, please start your post with [O].  Please check the sidebar for information about tagging your submission properly.

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Flair for [O] posts Non-Verified
    title (starts-with): ["[O]"]
    author:
        ~flair_text: ["verified"]
    set_flair: ["OFFERING", "offering"]

---

    # Flair for [O] posts Verified
    title (starts-with): ["[O]"]
    author:
        flair_text: ["verified"]
    set_flair: ["OFFERING_VERIFIED", "offering"]

---

    # Flair for [W] posts.
    title (starts-with): ["[W]"]
    set_flair: ["WANTED", "wanted"]

---

    # Flair for [O] posts when OP comment indicates that invites no longer offered
    type: comment
    parent_submission:
        title (starts-with): ["[O]"]
        overwrite_flair: true
        set_flair: ["NO MORE INVITES", "out"]
    body: [all gone, all invites are taken, all invites have been, all invites taken, all out, all out!, all out till next time, all sent, all taken, closed, Done, finished, gone, I'm all out of invites!, I'm out, I am out, invitations have been given, invites have been given, invites send, invites sent, no mas, no more, none left, out, "out.", Out for now!, out of invites, that's it]
    author:
        is_submitter: true
    is_top_level: false

---

    # Flair and lock [W] posts when OP comment indicates that invites no longer needed
    type: comment
    parent_submission:
        title (starts-with): ["[W]"]
        overwrite_flair: true
        set_flair: ["NO MORE INVITES", "out"]
        set_locked: true
    body: [all good, all okay, all set, "all set, thanks!", all sorted, am good, am set, close this, closed, completed, done, "done.", found one, filled, fulfilled, good to go, "good to go.", "good to go!", "good to go,", "Good to go :)", got a code, got a invite, got an invitation, got an invite, got invite, got it, got mine, got my invite, got one, got the invite, got the invites, got what I wanted, got your invitation, got your invite, gtg, has the invite, have the invite, hooked me up, hooked up, I got, I have one, I was offered a invite, I was offered an invite, Im good, "I'm good", invite received, "invite received!", "Invite received. Thanks!", invited, kind to give me a invite, kind to give me an invite, no invite needed, no longer needed, obtained, please close, post is closed, received, receved, recieved, "received an invite!", "received invite.", "received one. good to go thanks!", sent a invite, sent an invite, served to me, signed up, sorted, squared, taken care of, thank you, "that's all"]
    author:
        is_submitter: true
    is_top_level: false

---

    # Flair for [W] posts when OP comment indicates that invites no longer needed Regex
    type: comment
    parent_submission:
        title (starts-with): ["[W]"]
        overwrite_flair: true
        set_flair: ["NO MORE INVITES", "out"]
    body (regex): ['got the \w+ invite']
    author:
        is_submitter: true
    is_top_level: false

---

    # Remove phone numbers and send review message
    title+body (regex): ["\\(?(\\d{3})\\)?([ .-])(\\d{3})([ .-])(\\d{4})"]
    ~body+url (regex): ["(\\[[^\\]]+?\\]\\()?(https?://|www\\.)\\S+\\)?"]
    ~body+title+url (regex): ["(800|855|866|877|888)\\W*\\d{3}\\W*\\d{4}", "\\d{3}\\W*555\\W*\\d{4}", "999-999-9999", "000-000-0000", "123-456-7890", "111-111-1111", "012-345-6789", "888-888-8888", "867-5309"]
    action: remove
    action_reason: Remove phone numbers and send review message
    modmail_subject: AutoMod caught possible phone number being posted - please review!
    modmail: |
        **User:** /u/{{author}}

        **Type:** {{kind}}

        **Post Title:** {{title}}

        **Body/Comment**: {{body}}

---

    # Remove email addresses and send review message - A
    title+body (regex): ["\\w+@\\w+\\.\\w+"]
    action: remove
    action_reason: Remove email addresses and send review message - A ({{match}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites because you posted your email address publicly.

        Instead, please send your email address via personal message to the user offering invites.  This will keep things private and you safe.  Thank you!

---

    # Remove email addresses - B
    ## Example 1: My email address is [reddit username] @ gmail
    title+body (includes): ["(@)", " @ gmail", "@gmail", " at gmail", " @ hotmail", "@hotmail", " at hotmail", " @ outlook", "@outlook", " at outlook", " @ yahoo", "@yahoo", " at yahoo"]
    action: remove
    action_reason: Remove email addresses - B ({{match}})
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites because you posted your email address publicly.

        Instead, please send your email address via personal message to the user offering invites.  This will keep things private and you safe.  Thank you!

---

    # Remove posts with multiple title tags.
    ## OLD title (regex, includes): ["\\[[OHW]\\].*?\\[[OHW]\\]"]
    type: submission
    title (regex): ['\[[how]\].*\[(h|have|o|offer|offered|w|want|wanted)\]']
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: 3
    action: remove
    action_reason: Remove posts with multiple title tags.
    comment: |
        Your {{kind}} has been automatically removed from /r/UsenetInvites. We do not allow:

        * Selling or trading of invites
        * Posts containing both invite offers and requests (these should be in separate [W] / [O] posts)

        See https://www.reddit.com/r/UsenetInvites/about/rules

---

    # Remove comments from users with negative 10 karma.
    author:
        combined_karma: "< -10"
    action: remove
    action_reason: Remove comments from users with negative 10 karma.

---

    # Probably don't need anymore per /r/AutoModerator/comments/2bc6gx/automoderator_updates_mods_immune_to/
    # user_conditions:
    #    rank: moderator
    # action: approve

---

    # Comment when [O] post completed
    title (starts-with): ["[O]"]
    comment: |
        Once you are out of invites, please reply to this comment letting us know you are out.

        Thank you!

---

    # Comment when [W] post completed
    title (starts-with): ["[W]"]
    comment: |
        If you receive an invite, please reply to this message letting us know you are good to go.

        Thank you!

---

    # Rules Reminder for unverified [O] posts
    type: submission
    title (starts-with): ["[O]"]
    flair_text: ["OFFERING"]
    priority: -1
    comment: |
        **Offer Restrictions:** Reddit accounts responding to this offer must be at least 3 months old and and must have at least 30 comment karma. See the [sticky post](https://www.reddit.com/r/UsenetInvites/wiki/postinguidelines) for details.

        **Friendly Rules Reminder:** There is no trading, buying, or selling allowed. Please [send a message to the moderators](http://www.reddit.com/message/compose?to=%2Fr%2FUsenetInvites) if you encounter anyone attempting to break our community rules.

        See https://www.reddit.com/r/UsenetInvites/about/rules for all sub rules.

---

    # Rules Reminder for verified [O] posts
    type: submission
    title (starts-with): ["[O]"]
    flair_text: ["OFFERING_VERIFIED"]
    priority: -1
    comment: |
        **Friendly Rules Reminder:** There is no trading, buying, or selling allowed. Please [send a message to the moderators](http://www.reddit.com/message/compose?to=%2Fr%2FUsenetInvites) if you encounter anyone attempting to break our community rules.

        See https://www.reddit.com/r/UsenetInvites/about/rules for all sub rules.

---

    # Rules Reminder for [W] posts
    title (starts-with): ["[W]"]
    priority: -1
    comment: |
        **Friendly Rules Reminder:** There is no trading, buying, or selling allowed. Please [send a message to the moderators](http://www.reddit.com/message/compose?to=%2Fr%2FUsenetInvites) if you encounter anyone attempting to break our community rules.

        See https://www.reddit.com/r/UsenetInvites/about/rules for all sub rules.

---

    # Rules Reminder for Comments in [O] posts
    type: comment
    body: [can I have a, can I have an, dm, invite please, love to get one, message, messaged, please I need, pm, take a invite, take an invite, yes please]
    ~body#whitelist: [email received]
    parent_submission:
        title (starts-with): ["[O]"]
    author:
        comment_karma: "> 30"
        account_age: "> 90"
        satisfy_any_threshold: false
    author:
        is_submitter: false
    priority: -1
    comment: |
        **Friendly Rules Reminder:** Please leave a comment here if you receive an invite from OP.

---

    # Tip for [W] altHUB posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): ["alt hub", althub]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://althub.co.za/register for details.

---

    # Tip for [W] DOGnzb posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [dog]
    priority: -1
    comment: |
        **Tip:** To check if this indexer currently has open registration see https://dognzb.cr/register

---

    # Tip for [W] DuskyNZB posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [dusky]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://dusky.deepcave.net/register for details.

---

    # Tip for [W] LuluNZB posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [lulu]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://lulunzb.com/register for details.

---

    # Tip for [W] NG4You posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [ng4y, ngforyou]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See http://www.ng4you.com/?inscription for details.

---

    # Tip for [W] NZB.tv posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): ["nzb.tv", nzbtv]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://nzb.tv/register for details.

---

    # Tip for [W] NZBCat posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [cat]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://www.reddit.com/r/UsenetInvites/comments/2zagl2/o_nzbcat_invites/, https://nzb.cat/invites, & https://nzb.cat/register for details.

---

    # Tip for [W] NzbPlanet posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [planet]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://nzbplanet.net/register or https://nzbplanet.net/registerpremium for details.

---

    # Tip for [W] SimplyNZBs posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [simplynzb]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://simplynzbs.com/register for details.

---

    # Tip for [W] UsenetHD.li posts
    type: submission
    title (starts-with): ["[W]"]
    title#Indexer (includes): [usenethd]
    priority: -1
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://www.usenethd.li/register/ for details.

---

    # # Tip and Remove for NZB Finder posts
    type: submission
    title#Indexer (includes): [nzbfinder, nzb finder]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: -1
    action: remove
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://nzbfinder.ws/register for details.

---

    # Tip and Remove for GingaDADDY posts
    type: submission
    title#Indexer (includes): [ginga]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: -1
    action: remove
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://www.gingadaddy.com/signup.php for details.

---

    # Tip and Remove for Miatrix posts
    type: submission
    title#Indexer (includes): [miatrix]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: -1
    action: remove
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://www.miatrix.com/register for details.

---

    # Tip and Remove for nzb.su posts
    type: submission
    title#Indexer (includes): ["nzb su", "nzb.su", " .su", " . su"]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: -1
    action: remove
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://nzb.su/register for details.

---

    # Tip and Remove for NZBGeek posts
    type: submission
    title#Indexer (includes): [geek]
    overwrite_flair: true
    set_flair: ["NO MORE INVITES", "out"]
    set_locked: true
    priority: -1
    action: remove
    comment: |
        **Tip:** As an alternative if you are unable to receive an invite this indexer does offer other options to allow users to register directly.

        See https://nzbgeek.info/register.php for details.

---
