# SEO Guide: J. Sai Kumar (Ex-Army) LIC Website

## 1. Before you upload (2 minutes)
1. Copy your existing `images/` folder into this folder (it is not included in this zip).
2. Run: `python3 set-domain.py https://www.yourdomain.com`
   This replaces the placeholder domain in index.html, all plan pages, sitemap.xml and robots.txt.
   (Or use Find & Replace for `https://www.YOURDOMAIN.com`.)
3. Upload everything to your hosting root so that `yourdomain.com/sitemap.xml` and `yourdomain.com/robots.txt` open in the browser.

## 2. What was added
- Home page: SEO title, meta description, keywords, canonical, robots, Open Graph + Twitter tags
- One H1 and keyword-rich H2s, descriptive image alt text, lazy-loading
- FAQ section (8 questions) with FAQ schema, plus crawlable links to every plan in the footer
- Schema.org JSON-LD: InsuranceAgency/LocalBusiness, Person, WebSite, FAQPage
- 37 static plan pages in `plans/` (one URL per plan, own title/description/H1/H2s/breadcrumb schema)
- `sitemap.xml` (38 URLs), `robots.txt`, `404.html`, CSS moved to `css/style.css`
- Why static pages: the old `#plan-name` links are invisible to Google. The plan cards now open real pages.

## 3. After the site is live
1. Google Search Console (search.google.com/search-console): add your domain, verify (paste the tag into the commented line in index.html `<head>`), then Sitemaps > submit `sitemap.xml`.
2. Request indexing for the home page using URL Inspection.
3. Bing Webmaster Tools: import from Search Console, submit the same sitemap.
4. Google Business Profile: create a free profile for your Bengaluru/Chennai service area with the same name and phone numbers. This matters most for "LIC agent near me" searches.
5. Add your website link to your Facebook, Instagram and Telegram profiles.

## 4. Target keywords (already used in titles, headings and text)
Primary: LIC agent in Bengaluru, LIC agent in Chennai, LIC insurance advisor, ex-army LIC agent
Plans: LIC new plans 2026, LIC term insurance, LIC child plan, LIC pension plan, LIC endowment plan, LIC money back plan, LIC ULIP, plus each plan name (Jeevan Umang, Jeevan Utsav, Jeevan Amar, Bima Ratna, etc.)
Other: health insurance advisor, Star Health insurance, general insurance, LIC agent code 0241770N
Tip: Google ignores the meta keywords tag. Rankings come from the visible text, headings, titles and links above.

## 5. Keep in mind
- Adding a new plan: add it to `PLANS` in index.html, then create its page in `plans/` (copy an existing one) and add it to sitemap.xml. Update `lastmod` dates when you edit pages.
- Never copy text from licindia.in word-for-word; Google penalises duplicate content.
- Do not add fake reviews or ratings; Google may penalise the site. Real Google Business reviews are the safe way.
- SEO takes weeks to months. Check Search Console monthly.
