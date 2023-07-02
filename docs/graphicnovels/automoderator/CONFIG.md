##### ANTI-SPAM RULES #####
#
# Rules for combatting spam on this subreddit.
#
### USERS ###
#
# AutoMod ban; useful for spammers who submit to multiple domains.
#
author:
    name: [example]
action: spam

---

### DOMAINS ###
domain: [example.com, example2.com]
action: spam

---

### PIRACY ###
# No Piracy!
# Courtesy of u/manyamile and the DCcomics mods
    domain+body+title: [comicextra.com, comicsnake.com, comix-load.in, libgen.fun, libgen.rs, mygully.com, ViewComic.com, viewcomics.me, viewcomicsonline.com, getcomics.info, mygully.com, readallcomics.com, readcomiconline.li, readcomiconline.to, readcomicsonline.ru, xoxocomics.com, torrent, isohunt.to, seedpeet.me, kickass.to, torlock.com, take.fm, torrentfunk.com, thepiratebay.se, torrents.to, vcdq.com, torrentcrazy.com, houndmirror.com, thunderbytes.net, fulldls.com, limetorrents.com, comix4free.com, movie4k.to, watchcartoononline.com, popcorntime.io, kickass.to, demonoid.ph, extratorrent.cc, torrentz.com, yts.re, eztv.it, 1337x.to, bitsnoop.com, rarbg.com, animeflavor.com, viewcomic.com, 4shared.com, deadpoolsupplier.imgur.com, comicastle.org, readcomiconline.com, read-comic.com, comicextra.com, flixtor.is, kimcartoon.me, fmovie.sc]
    action: filter
    action_reason: "Piracy link"
    modmail: "User posted a known piracy link: [{{match}}]. Review and warn user."

---

# Amazon Affiliate Link Ban
standard: amazon affiliate links
action: spam
comment: Your {{kind}} was removed because Amazon affiliate links are not allowed.

---

### PHRASES ###
#
# These phrases, in submissions are often spammy and if not, rarely provide any useful content. If the user is not an approved submitter,
# automatically mark these phrases as spam.
#
type: submission
author:
    is_contributor: false
title+body (regex):
     - '(dubai|singapore|pune|india|palm beach|burnbury|gurgaon|noida|bhasin|morningside|mumbai|corona|ecnon|rosal|russell|plumas|chino|pacific grove|olivehurst|brisbane|toulouse|bhartiya|nikoo|aditya|niketan|manesar|caribbean|alpharetta|kilda|gozo|malta|noida|calgary|agence)' # spammy places
     - 'residential (flat|builder)s?'
     - 'luxury (apartments|condomnium)s?'
     - 'ceebros|ambattur|imperiale|ghaxiabad|tgs|cerritos|srk|killeen|thailand|bangkok|bhk|bangalor|Kharadi'
     - '(/?r/)?(realestatetechnology|retech)'
     - 'bigger ?pockets(.com)?'
     - '((moneyunder|retireby)(3|4)0)|getrichslowly'
     - 'invest ?four ?more'
action: spam

---

# Comment report alert and removal
type: comment
reports: 2
action: remove
modmail: The above comment has received 2 reports, please check on it.

---

# auto-remove new account submissions
type: submission
author:
    satisfy_any_threshold: true
    comment_karma: "< 5"
    account_age: "< 7 days"
action: remove

---

type: comment
author:
    post_karma: "< -50"
action: filter
modmail_subject: "low karma"
modmail: |
    "Check the modqueue to approve the comment, or review it in context here: {{permalink}}.

    Comment: {{body}}"
---

# Auto request for a comment on image posts
type: link submission
domain: [i.redd.it, imgur.com]
comment: |
    "It looks like you have posted an image.

    Rule #7 of this community requires image posts to be accompanied by some substantial information about what the image shows. This should be more meaningful than just "here's my collection" or "I've bought this". For example, share your thoughts about whatever is in the image, or ask a question about it. If you haven't already provided such text in the post itself, please do so in a comment. If your post doesn't comply with rule #7 within 15 minutes of receiving this comment, it may be removed.

    If this is not an image post, please ignore this comment."

comment_stickied: true
comment_locked: true

---
