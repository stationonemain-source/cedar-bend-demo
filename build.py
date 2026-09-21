"""Builds the Cedar Bend demo pages. One layout, seven pages. Run: python build.py"""
import pathlib, html

TOWN = "Cedar Bend"
SEAL = '''<svg class="seal" viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="20" fill="none" stroke="currentColor" stroke-width="2"/><path d="M22 9l9 12h-5v11h-8V21h-5z" fill="currentColor"/><path d="M12 33h20" stroke="currentColor" stroke-width="2"/></svg>'''
ICON = {
 "pay": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h3"/></svg>',
 "agenda": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="4" y="4" width="16" height="17" rx="2"/><path d="M8 2v4M16 2v4M4 10h16M8 14h5"/></svg>',
 "report": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17h.01"/></svg>',
 "permit": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h6M9 16h6"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4"/></svg>',
 "warn": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17h.01"/></svg>',
}
NAV = [("index.html","Home"),("pay.html","Pay a bill"),("meetings.html","Agendas & minutes"),("report.html","Report a problem"),("departments.html","Departments"),("news.html","News")]

def layout(file, title, body, desc):
    cur = ' aria-current="page"'
    nav = "".join(f'<li><a href="{h}"{cur if h==file else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | City of {TOWN}, Texas</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,600&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<aside class="demo" aria-label="Demonstration notice">Demonstration site by Quorum. Cedar Bend is a fictional town; every name, date and number here is sample content. <a href="https://quorumcompliance.com">quorumcompliance.com</a></aside>
<section class="alert" aria-label="Service alert"><div class="wrap">{ICON["warn"]}<span><strong>Water main repair on Pecan St.</strong> Low pressure expected Tuesday, Sept 22, 8 a.m. to noon. <a href="news.html#pecan">Details</a></span></div></section>
<header class="top"><div class="wrap">
  <a class="logo" href="index.html">{SEAL}<span><b>{TOWN}</b><span>Texas</span></span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav aria-label="Main"><ul class="nav" id="nav">{nav}</ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
 <div class="fgrid">
  <div><h2>City Hall</h2><p>210 W. Main Street<br>Cedar Bend, TX 76000<br>Monday to Friday, 8 a.m. to 5 p.m.</p><p><a href="tel:+15125550140">(512) 555-0140</a><br><a href="mailto:cityhall@cedarbendtx.gov">cityhall@cedarbendtx.gov</a></p></div>
  <div><h2>Popular</h2><ul><li><a href="pay.html">Pay a water bill</a></li><li><a href="meetings.html">Council agendas</a></li><li><a href="report.html">Report a problem</a></li><li><a href="departments.html#records">Request a record</a></li></ul></div>
  <div><h2>About this site</h2><ul><li><a href="accessibility.html">Accessibility</a></li><li><a href="news.html">News and notices</a></li><li><a href="departments.html">All departments</a></li></ul></div>
 </div>
 <div class="legal">City of Cedar Bend, Texas. This site is tested against WCAG 2.1 AA. If something here does not work for you, tell us at <a href="accessibility.html">the accessibility page</a> and we will fix it or give you the information another way.</div>
</div></footer>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');if(!b||!n)return;b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');}});}})();
</script>
</body>
</html>'''

PAGES = {}

PAGES["index.html"] = ("Home", "Pay a bill, find a meeting agenda, report a problem, or apply for a permit. The official website of the City of Cedar Bend, Texas.", f'''
<section class="hero"><div class="wrap">
 <h1>What do you need today?</h1>
 <p class="lede">Most people come here for one of four things. They are right below, and they work on your phone.</p>
 <ul class="tasks">
  <li><a href="pay.html">{ICON["pay"]}<b>Pay a water bill</b><span>Card or bank account. No account needed, just your bill number.</span></a></li>
  <li><a href="meetings.html">{ICON["agenda"]}<b>Agendas and minutes</b><span>City Council, Planning and Zoning. Posted 72 hours ahead.</span></a></li>
  <li><a href="report.html">{ICON["report"]}<b>Report a problem</b><span>Potholes, streetlights, water leaks, code concerns.</span></a></li>
  <li><a href="departments.html#permits">{ICON["permit"]}<b>Permits and forms</b><span>Building, yard sale, park pavilion, records requests.</span></a></li>
 </ul>
 <form class="search" role="search" action="#" method="get"><label for="q" class="skip">Search the site</label><input id="q" name="q" type="text" placeholder="Search, for example “trash pickup”"><button class="btn" type="submit">Search</button></form>
</div></section>

<section><div class="wrap split">
 <div class="card meeting" aria-labelledby="nm">
  <span class="tag ok">Next meeting</span>
  <h2 id="nm" style="margin-top:8px">City Council regular meeting</h2>
  <time datetime="2026-10-06T18:00">Tuesday, Oct 6, 6:00 p.m.</time>
  <dl><dt>Where</dt><dd>Council Chambers, City Hall, 210 W. Main St.</dd><dt>Agenda</dt><dd>Posted by Friday, Oct 2 at 6 p.m.</dd><dt>Speak</dt><dd>Sign in before 6 p.m. Three minutes per person.</dd></dl>
  <a class="btn ghost" href="meetings.html">All meetings</a>
 </div>
 <div>
  <h2>News and notices</h2>
  <ul class="news">
   <li><time datetime="2026-09-18">September 18</time><a href="news.html#pecan">Pecan Street water main repair scheduled for Sept 22</a></li>
   <li><time datetime="2026-09-15">September 15</time><a href="news.html#budget">Council adopts the 2026–27 budget; tax rate unchanged at $0.4821</a></li>
   <li><time datetime="2026-09-09">September 9</time><a href="news.html#bulk">Fall bulk trash pickup: north of Main on Oct 12, south of Main on Oct 13</a></li>
   <li><time datetime="2026-09-02">September 2</time><a href="news.html#pool">Cedar Bend pool closes for the season Sept 7</a></li>
  </ul>
  <a href="news.html">All news and public notices</a>
 </div>
</div></section>

<section class="band"><div class="wrap">
 <h2>Departments</h2>
 <p class="muted">Who to call, and what they handle.</p>
 <ul class="depts">
  <li><a href="departments.html#utilities"><b>Water and utilities</b><span>Billing, new service, leaks, disconnects</span></a></li>
  <li><a href="departments.html#streets"><b>Public works</b><span>Streets, drainage, trash and recycling</span></a></li>
  <li><a href="departments.html#police"><b>Police</b><span>Non-emergency line, reports, records</span></a></li>
  <li><a href="departments.html#permits"><b>Building and permits</b><span>Inspections, zoning, code compliance</span></a></li>
  <li><a href="departments.html#parks"><b>Parks and recreation</b><span>Pavilion rentals, pool, youth sports</span></a></li>
  <li><a href="departments.html#records"><b>City Secretary</b><span>Records requests, elections, council support</span></a></li>
 </ul>
</div></section>

<section><div class="wrap hours">
 <div><b>City Hall</b>Mon to Fri, 8 a.m. to 5 p.m.</div>
 <div><b>Utility payments</b>Drive-through open until 5:30 p.m.</div>
 <div><b>Trash pickup</b>Tuesdays. Recycling every other Tuesday.</div>
 <div><b>Emergency</b>Call 911. Non-emergency police (512) 555-0150.</div>
</div></section>
''')

PAGES["pay.html"] = ("Pay a bill", "Pay your Cedar Bend water, sewer and trash bill online, by phone, by mail or in person.", f'''
<div class="page-head"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Pay a bill</div><h1>Pay a water bill</h1><p class="lede">One bill covers water, sewer and trash. Due on the 15th. A 10% late fee applies after the 25th.</p></div></div>
<div class="wrap content grid2">
 <div>
  <h2>Online, in about a minute</h2>
  <ol class="steps">
   <li><div><b>Find your account number</b><br>It is in the top right of your paper bill, eight digits.</div></li>
   <li><div><b>Open the payment portal</b><br>You will leave this site for the City's payment processor. There is a $1.50 convenience fee for cards; bank drafts are free.</div></li>
   <li><div><b>Keep the confirmation email</b><br>Payments post the next business day.</div></li>
  </ol>
  <a class="btn" href="#" aria-describedby="ext">Pay online now</a>
  <p id="ext" class="small muted" style="margin-top:10px">Opens the City's payment processor in a new page. (Demo: link disabled.)</p>
  <h2>Set up autopay</h2>
  <p>Bring a voided check to City Hall or download the <a class="doc" href="#">{ICON["doc"]} bank draft form (PDF, 1 page)</a>. Drafts run on the 15th.</p>
 </div>
 <div>
  <h2>Other ways to pay</h2>
  <table><caption>Where and when</caption><tr><th scope="row">By phone</th><td>(512) 555-0141, 24 hours, automated. Card only.</td></tr><tr><th scope="row">Drive-through</th><td>City Hall, north side. Mon to Fri, 8 a.m. to 5:30 p.m.</td></tr><tr><th scope="row">Drop box</th><td>Beside the drive-through. Checked at 8 a.m. daily. No cash.</td></tr><tr><th scope="row">By mail</th><td>P.O. Box 88, Cedar Bend, TX 76000. Postmark counts.</td></tr></table>
  <h2>Trouble paying?</h2>
  <p>Call utility billing before the 25th and ask for a payment arrangement. One extension per year, no questions asked. <a href="tel:+15125550142">(512) 555-0142</a></p>
 </div>
</div>
''')

PAGES["meetings.html"] = ("Agendas and minutes", "City Council and board agendas, packets and minutes for the City of Cedar Bend, posted at least 72 hours before each meeting.", f'''
<div class="page-head"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Agendas and minutes</div><h1>Agendas and minutes</h1><p class="lede">Agendas are posted at least 72 hours before a meeting, as Texas open meetings law requires. Minutes are posted after the council approves them, usually at the next meeting.</p></div></div>
<div class="wrap content">
 <h2>Upcoming</h2>
 <table>
  <caption>Next 30 days</caption>
  <thead><tr><th scope="col">Date</th><th scope="col">Body</th><th scope="col">Documents</th></tr></thead>
  <tbody>
  <tr><td><time datetime="2026-10-06T18:00">Oct 6, 6:00 p.m.</time></td><td>City Council, regular</td><td><span class="tag">Agenda posted by Oct 2</span></td></tr>
  <tr><td><time datetime="2026-10-13T18:30">Oct 13, 6:30 p.m.</time></td><td>Planning and Zoning Commission</td><td><span class="tag">Agenda posted by Oct 9</span></td></tr>
  <tr><td><time datetime="2026-10-20T18:00">Oct 20, 6:00 p.m.</time></td><td>City Council, regular</td><td><span class="tag">Agenda posted by Oct 16</span></td></tr>
  </tbody>
 </table>
 <h2>Recent</h2>
 <table>
  <caption>City Council, 2026</caption>
  <thead><tr><th scope="col">Date</th><th scope="col">Agenda</th><th scope="col">Packet</th><th scope="col">Minutes</th></tr></thead>
  <tbody>
  <tr><td>Sept 15</td><td><a class="doc" href="#">{ICON["doc"]} Agenda (PDF, 2 pages)</a></td><td><a class="doc" href="#">{ICON["doc"]} Packet (PDF, 48 pages)</a></td><td><span class="tag">Pending approval</span></td></tr>
  <tr><td>Sept 1</td><td><a class="doc" href="#">{ICON["doc"]} Agenda (PDF, 2 pages)</a></td><td><a class="doc" href="#">{ICON["doc"]} Packet (PDF, 31 pages)</a></td><td><a class="doc" href="#">{ICON["doc"]} Minutes (PDF, 4 pages)</a></td></tr>
  <tr><td>Aug 18</td><td><a class="doc" href="#">{ICON["doc"]} Agenda (PDF, 3 pages)</a></td><td><a class="doc" href="#">{ICON["doc"]} Packet (PDF, 62 pages)</a></td><td><a class="doc" href="#">{ICON["doc"]} Minutes (PDF, 5 pages)</a></td></tr>
  <tr><td>Aug 4</td><td><a class="doc" href="#">{ICON["doc"]} Agenda (PDF, 2 pages)</a></td><td><a class="doc" href="#">{ICON["doc"]} Packet (PDF, 27 pages)</a></td><td><a class="doc" href="#">{ICON["doc"]} Minutes (PDF, 3 pages)</a></td></tr>
  </tbody>
 </table>
 <p class="small muted">Every PDF posted since this site launched is tagged for screen readers and has a real title. Older documents are in the <a href="#">archive</a>, and we will convert any of them on request.</p>
 <h2>Speaking at a meeting</h2>
 <p>Sign the sheet at the chamber door before the meeting starts. You get three minutes on any item, or on anything not on the agenda during citizen comment. The council cannot discuss or act on items that are not on the posted agenda, but it can ask staff to follow up.</p>
</div>
''')

PAGES["report.html"] = ("Report a problem", "Report a pothole, streetlight, water leak or code concern to the City of Cedar Bend.", f'''
<div class="page-head"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Report a problem</div><h1>Report a problem</h1><p class="lede">Potholes, streetlights, water leaks, stray animals, high grass, missed trash. Tell us where and we will get it to the right crew. You get a ticket number by email.</p><p><strong>Emergency, or water gushing?</strong> Call <a href="tel:911">911</a> or the after-hours utility line, <a href="tel:+15125550149">(512) 555-0149</a>.</p></div></div>
<div class="wrap content">
 <form class="std" action="#" method="post" novalidate>
  <fieldset><legend>What is it?</legend>
   <div class="choice"><input type="radio" id="t1" name="type" value="street"><label for="t1" style="margin:0;font-weight:400">Street, sidewalk or drainage</label></div>
   <div class="choice"><input type="radio" id="t2" name="type" value="light"><label for="t2" style="margin:0;font-weight:400">Streetlight out</label></div>
   <div class="choice"><input type="radio" id="t3" name="type" value="water"><label for="t3" style="margin:0;font-weight:400">Water or sewer</label></div>
   <div class="choice"><input type="radio" id="t4" name="type" value="trash"><label for="t4" style="margin:0;font-weight:400">Trash or recycling missed</label></div>
   <div class="choice"><input type="radio" id="t5" name="type" value="code"><label for="t5" style="margin:0;font-weight:400">Property or code concern</label></div>
   <div class="choice"><input type="radio" id="t6" name="type" value="other"><label for="t6" style="margin:0;font-weight:400">Something else</label></div>
  </fieldset>
  <label for="where">Where is it? <span class="req" aria-hidden="true">*</span></label>
  <p class="hint" id="where-h">A street address or the nearest cross streets.</p>
  <input id="where" name="where" type="text" required aria-describedby="where-h" autocomplete="street-address">
  <label for="what">What is happening? <span class="req" aria-hidden="true">*</span></label>
  <textarea id="what" name="what" rows="4" required></textarea>
  <label for="photo">Photo (optional)</label>
  <input id="photo" name="photo" type="file" accept="image/*">
  <label for="email">Your email <span class="req" aria-hidden="true">*</span></label>
  <p class="hint" id="email-h">So we can send the ticket number and tell you when it is done.</p>
  <input id="email" name="email" type="email" required aria-describedby="email-h" autocomplete="email">
  <label for="phone">Phone (optional)</label>
  <input id="phone" name="phone" type="tel" autocomplete="tel">
  <p class="small muted">Required fields are marked with an asterisk. We do not share your details, and you can report anonymously by leaving the contact fields blank; you just won't get updates.</p>
  <button class="btn" type="submit">Send the report</button>
 </form>
</div>
''')

PAGES["departments.html"] = ("Departments", "Every City of Cedar Bend department, what it handles, and how to reach it.", f'''
<div class="page-head"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Departments</div><h1>Departments</h1><p class="lede">One phone number reaches all of them: <a href="tel:+15125550140">(512) 555-0140</a>. Direct lines and what each office handles are below.</p></div></div>
<div class="wrap content">
 <section id="utilities"><h2>Water and utilities</h2><p>Billing, new service, disconnects, leaks on the City side of the meter. Direct line <a href="tel:+15125550142">(512) 555-0142</a>. <a href="pay.html">Pay a bill</a>. To start service, bring a photo ID and a lease or deed; a $100 deposit is refunded after 12 on-time payments.</p></section>
 <section id="streets"><h2>Public works</h2><p>Streets, drainage, signs, trash and recycling. Trash is picked up Tuesdays; put the cart out by 7 a.m. Recycling runs every other Tuesday. <a href="report.html">Report a pothole or missed pickup</a>.</p></section>
 <section id="police"><h2>Police</h2><p>Emergency: 911. Non-emergency <a href="tel:+15125550150">(512) 555-0150</a>. Accident reports are available three business days after the incident at the front desk, 400 E. Main St.</p></section>
 <section id="permits"><h2>Building and permits</h2><p>Building permits, inspections, zoning questions and code compliance. Most residential permits (fences, sheds, water heaters) are issued the same day if the form is complete.</p>
 <ul><li><a class="doc" href="#">{ICON["doc"]} Residential building permit application (PDF, 2 pages)</a></li><li><a class="doc" href="#">{ICON["doc"]} Yard sale permit (free, online form)</a></li><li><a class="doc" href="#">{ICON["doc"]} Fee schedule 2026–27 (PDF, 3 pages)</a></li></ul></section>
 <section id="parks"><h2>Parks and recreation</h2><p>Pavilion rentals at Cedar Bend Park are $40 for residents, $75 for non-residents, first come first served by phone. The pool is open Memorial Day to Labor Day.</p></section>
 <section id="records"><h2>City Secretary</h2><p>Public information requests, elections, ordinances, council support. Under the Texas Public Information Act, most requests are answered within 10 business days. Email <a href="mailto:records@cedarbendtx.gov">records@cedarbendtx.gov</a> or use the <a class="doc" href="#">{ICON["doc"]} records request form (online)</a>.</p></section>
</div>
''')

PAGES["news.html"] = ("News and notices", "News, public notices and service alerts from the City of Cedar Bend.", f'''
<div class="page-head"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / News</div><h1>News and notices</h1><p class="lede">Service alerts, council decisions and legal notices, newest first. Get these by text: send CEDAR to (512) 555-0199. (Demo number.)</p></div></div>
<div class="wrap content">
 <article id="pecan"><h2>Pecan Street water main repair scheduled for Sept 22</h2><p class="small muted"><time datetime="2026-09-18">September 18, 2026</time></p><p>Crews will replace a 6-inch main between 3rd and 5th on Tuesday, September 22, from 8 a.m. to about noon. Homes on Pecan, 4th and the 300 block of Elm will have low pressure or no water during the work. Run a cold tap for two minutes afterward if the water looks cloudy. Questions: <a href="tel:+15125550142">(512) 555-0142</a>.</p></article>
 <article id="budget"><h2>Council adopts the 2026–27 budget; tax rate unchanged</h2><p class="small muted"><time datetime="2026-09-15">September 15, 2026</time></p><p>The council adopted a $6.4 million budget on Tuesday and kept the property tax rate at $0.4821 per $100 of value. The budget adds one police officer and funds the Pecan Street water line. <a class="doc" href="#">{ICON["doc"]} Adopted budget (PDF, 58 pages)</a></p></article>
 <article id="bulk"><h2>Fall bulk trash pickup</h2><p class="small muted"><time datetime="2026-09-09">September 9, 2026</time></p><p>North of Main Street: Monday, October 12. South of Main: Tuesday, October 13. Set items at the curb the night before. No tires, paint or appliances with refrigerant.</p></article>
 <article id="pool"><h2>Pool closes for the season Sept 7</h2><p class="small muted"><time datetime="2026-09-02">September 2, 2026</time></p><p>Last swim is Labor Day. Thank you to the 14 lifeguards who worked this summer. Season passes for 2027 go on sale in April.</p></article>
</div>
''')

PAGES["accessibility.html"] = ("Accessibility", "How the City of Cedar Bend website is tested for accessibility and how to report a problem.", '''
<div class="page-head"><div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / Accessibility</div><h1>Accessibility</h1><p class="lede">This website is built to meet WCAG 2.1 Level AA, the standard adopted by the Department of Justice's ADA Title II rule for state and local governments.</p></div></div>
<div class="wrap content">
 <h2>What that means in practice</h2>
 <ul><li>Every page works with a keyboard alone and with screen readers such as NVDA, JAWS and VoiceOver.</li><li>Text can be enlarged to 200% without losing content.</li><li>Colors meet the required contrast, and no information is carried by color alone.</li><li>Documents posted since launch are tagged PDFs with real titles, headings and image descriptions.</li><li>The site is re-tested every quarter, and after any major change.</li></ul>
 <h2>Something not working for you?</h2>
 <p>Tell us. Email <a href="mailto:accessibility@cedarbendtx.gov">accessibility@cedarbendtx.gov</a> or call <a href="tel:+15125550140">(512) 555-0140</a>. Say which page or document, and what happened. We will fix it or provide the information in another format within five business days.</p>
 <h2>Older documents</h2>
 <p>Some PDFs from before this site launched are not yet accessible. If you need one, ask and we will convert it, usually within two business days.</p>
 <h2>Last review</h2>
 <p>Automated and manual review completed September 2026. (Demo: in a real deployment the date, tool and reviewer are listed here.)</p>
</div>
''')

out = pathlib.Path(__file__).parent
for f,(title,desc,body) in PAGES.items():
    (out/f).write_text(layout(f,title,body,desc),encoding="utf-8")
print("built",len(PAGES),"pages")
