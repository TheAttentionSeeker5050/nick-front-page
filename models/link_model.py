class Link:
    def __init__(self, link_label, link_url, link_icon_name, category):
        self.link_label = link_label
        self.link_url = link_url
        self.link_icon_name = link_icon_name
        self.category = category

    def to_dict(self):
        return {
            "link_label": self.link_label,
            "link_url": self.link_url,
            "link_icon_name": self.link_icon_name,
            "category": self.category
        }