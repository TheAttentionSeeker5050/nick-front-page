// mongo 

// use frontPageDB;
db = db.getSiblingDB('frontPageDB');

// the social media links
db.links.insertMany([
  {
    "link_label": "LinkedIn",
    "link_url": "https://www.linkedin.com/in/nicolas-castellano-dev/",
    "link_icon_name": "linkedin.svg",
    "category": "social"
  },
  {
    "link_label": "GitHub",
    "link_url": "https://github.com/TheAttentionSeeker5050",
    "link_icon_name": "github.svg",
    "category": "social"
  },
  {
    "link_label": "My Personal Website",
    "link_url": "https://nicolas-castellano.com/portfolio",
    "link_icon_name": "globe.svg",
    "category": "social"
  }
]);

// the project links
db.links.insertMany([
  {
    "link_label": "Firebase and Next.js Chat Application",
    "link_url": "https://next-chat-app-25od.onrender.com/",
    "link_icon_name": "project.svg",
    "category": "project"
  },
  {
    "link_label": ".NET Links Dashboard",
    "link_url": "https://links-dashboard.nicolas-castellano.com/",
    "link_icon_name": "project.svg",
    "category": "project"
  },
  {
    "link_label": "Vue.js Giphy API Explorer using",
    "link_url": "https://giphy-api-explorer-54465.netlify.app/",
    "link_icon_name": "project.svg",
    "category": "project"
  },
  {
    "link_label": "Vue.js World of Calculators",
    "link_url": "https://world-of-calculators.netlify.app/",
    "link_icon_name": "project.svg",
    "category": "project"
  },
  {
    "link_label": "Next.js, Golang, OAuth2, and MongoDB E-commerce Website",
    "link_url": "https://ecommerce-x.alligatorcode.pro/",
    "link_icon_name": "project.svg",
    "category": "project"
  },  
  {
    "link_label": "Django, JQuery and Tailwind CSS Job Posting Website",
    "link_url": "https://panda-jobs.nicolas-castellano.com/",
    "link_icon_name": "project.svg",
    "category": "project"
  }
])
