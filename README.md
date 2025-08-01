# Court Data Fetcher & Dashboard

This is a mini web app that simulates the process of fetching and displaying court case data based on user input. It was built as part of the Think Act Rise Foundation internship assessment.

---

##  Court Chosen

I selected the **eCourts Services Portal**  
🔗 https://services.ecourts.gov.in/ecourtindia_v6/

This portal provides case information for all District & Taluka courts in India via options like CNR number, party name, etc.

> However, due to **CAPTCHA protection** and **dynamic form rendering using JavaScript**, real-time scraping was not feasible without violating the site's automation policies.

Hence, I have:
- Simulated the backend scraping logic
- Parsed placeholder/dummy HTML structure
- Demonstrated the full app flow (form input → result display → PDF link)
- Explained how real scraping can be added using tools like **Playwright + manual CAPTCHA input or solver services**

---

##  Tech Stack

- Python 3
- Flask (Web framework)
- BeautifulSoup (HTML parsing)
- SQLite (Database)
- HTML/CSS (Frontend)

---

##  Features

- Input form: Case Type, Case Number, Filing Year
- Simulated court data fetching
- Display of:
  - Parties’ names
  - Filing & next hearing dates
  - Latest order/judgment PDF link
- Query logging in SQLite database
- Graceful error handling

---

##  How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/court-data-app.git
cd court-data-app
