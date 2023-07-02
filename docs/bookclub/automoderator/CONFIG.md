    # Auto-approve self-posts
    domain: "self.bookclub"
    action: approve

---

    # Send an alert to modmail if anything gets 1+ reports
    reports: 1
    modmail: The above item has received 1+ reports, please investigate.

---

    # Automatically remove anything that gets 2+ reports and send modmail
    # changed from 4 to 2 Jan 2017, Earthsophagus
    reports: 2
    action: remove
    modmail: The above item was automatically removed due to receiving 2+ reports. Please verify that this action was correct.

---

    # Remove amazon affiliate links.
    standard: amazon affiliate links
    action: spam
    comment: Your submission has been automatically removed because we do not allow affiliate links in /r/bookclub.
    modmail: The above item was automatically removed due to amazon affiliate link.

---

    # Domain blacklist
    domain: [leopardkingsaga.com]
    action: spam

---

    #1 Flair setting
    title: [ "[Brothers Karamazov]", "[Dune]", "[Poem of the Week]", "[To The Lighhouse]", "[Vote]", "[Chosen]" ]
    set_flair: ["{{match}}"]
    overwrite_flair: false
