user_agent = "Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [ja]"
headers = {
  "User-Agent": user_agent,
  "Accept-Language": "en-US,en;q=0.5"
}
       
def send_query(self, query):
  session = requests.Session()

  # consent to cookie collection stuff
  # just the default values for declining
  # except i removed as many as possible and changed some
  res = session.post("https://consent.google.com/save", headers=self.headers, data={
    "set_eom": True,
    "uxe": "none",
    "hl": "en",
    "pc": "srp",
    "gl":"DE",
    "x":"8",
    "bl":"user",
    "continue":"https://www.google.com/"
  })

  # actually send http request
  res = session.get(f"https://www.google.com/search?hl=en&q={parse.quote(query)}", headers=self.headers)

  return res.text
