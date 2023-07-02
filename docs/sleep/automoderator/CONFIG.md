    # Auto-approve self-posts
    domain: "self.sleep"
    action: approve

---

    # Send an alert to modmail if anything gets 10+ reports
    reports: 10
    modmail: The above item has received 10+ reports, please investigate.

---

    # Automatically remove anything that gets 3+ reports and send modmail
    reports: 3
    action: remove
    modmail: The above item was automatically removed due to receiving 3+ reports. Please verify that this action was correct.

---

    # Remove Crowdfunding Sites
    standard: crowdfunding sites
    action: remove

---

    # Remove Amazon Affiliate Links
    standard: amazon affiliate links
    action: remove
