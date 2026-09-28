#!/usr/bin/env python3
"""Build the full phyllux.org static mission hub from Round 3 page map."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
STAGING = ASSETS / "staging"
CSS = ROOT / "css"
CURSOR_ASSETS = Path(r"C:\Users\phibr\.cursor\projects\d-WS\assets")
PITCH_ASSETS = Path(
    r"D:\WS\communications\people\paul-mattys-place\quantonics-pitch-2026-09-14\assets"
)

# slug -> (title, lede, body_html_extra, hero_image_or_None, show_medical_disclaimer)
PAGES: list[dict] = []


def page(
    slug: str,
    title: str,
    lede: str,
    body: str,
    hero: str | None = None,
    medical: bool = False,
    section: str = "Missions",
) -> None:
    PAGES.append(
        {
            "slug": slug,
            "title": title,
            "lede": lede,
            "body": body,
            "hero": hero,
            "medical": medical,
            "section": section,
        }
    )


# --- define all pages from Round 3 union + mega appendix ---
page(
    "index",
    "Phyllux Tech",
    "Missions for flourishing people who can trust. Local first craft, honest tools, and a public door into apps, books, recovery education, Eco-Earn, shops, and institutional literacy.",
    """
    <div class="tile-grid">
      <a class="tile" href="recovery/"><img src="assets/org-hero-recovery.png" alt=""/><span>Recovery</span><em>Non clinical support tools</em></a>
      <a class="tile" href="parkinsons/"><img src="assets/org-hero-parkinsons.png" alt=""/><span>Parkinsons support education</span><em>Family and caregiver resources</em></a>
      <a class="tile" href="eco-earn/"><img src="assets/org-hero-eco-earn.png" alt=""/><span>Eco-Earn</span><em>Recycling gamification</em></a>
      <a class="tile" href="books/"><img src="assets/org-hero-books.png" alt=""/><span>Books</span><em>Phyllux Tech and Sproule Lit shelf</em></a>
      <a class="tile" href="suite/"><img src="assets/org-hero-apps.png" alt=""/><span>Quanton Suite</span><em>One mega app on phyllux.app</em></a>
      <a class="tile" href="lab/"><img src="assets/org-hero-lab.png" alt=""/><span>Lab</span><em>3D print, CAD, prototyping</em></a>
      <a class="tile" href="studio/"><img src="assets/org-hero-studio.png" alt=""/><span>Studio</span><em>Install, mix, master</em></a>
      <a class="tile" href="build-it/"><img src="assets/org-hero-build-it.png" alt=""/><span>Build and IT</span><em>PCs, web, staffing</em></a>
      <a class="tile" href="vst/"><img src="assets/org-hero-vst.png" alt=""/><span>VST Audio</span><em>Plugins and samples</em></a>
      <a class="tile" href="institutions/"><img src="assets/org-hero-institutions.png" alt=""/><span>Institutions</span><em>Schools, gov, business, hospital admin</em></a>
      <a class="tile" href="community/"><img src="assets/org-hero-community.png" alt=""/><span>Community</span><em>Events and Chautauqua</em></a>
      <a class="tile" href="roadmap/"><img src="assets/org-hero-roadmap.png" alt=""/><span>Roadmap</span><em>12 quarters and beyond</em></a>
    </div>
    <p class="note">Also explore privacy, careers, Edmonton, partners, academy, merch, donate, press, and legal. Soft launch: honest stubs first, then depth.</p>
    """,
    hero="org-hero-home.png",
    section="Home",
)

page("recovery", "Recovery", "Non clinical recovery support: journaling, logistics, community resources, and lived experience with consent.",
     """
     <ul>
       <li><a href="../recovery/journal/">Daily journal templates and prompts</a></li>
       <li><a href="../recovery/community/">Moderated peer community</a></li>
       <li><a href="../recovery/logistics/">Practical daily and appointment logistics</a></li>
       <li><a href="../recovery/stories/">Lived experience stories (consent required)</a></li>
       <li><a href="../recovery/resources/">Resource directory</a></li>
     </ul>
     <p>Related: <a href="../finally-me/">Finally Me</a> · <a href="https://phyllux.com/today.html">Today notebook</a></p>
     """,
     "org-hero-recovery.png", True)

page("recovery/journal", "Recovery journal", "Private journaling templates and prompts for recovery oriented check ins.",
     "<p>Local first by design. No clinical diagnosis. Templates for morning check in, meeting notes, gratitude, and urge surfing logs.</p>",
     "org-hero-recovery.png", True)
page("recovery/community", "Recovery community", "Moderated peer forums and circle tools.",
     "<p>Community is opt in. Moderation first. No medical advice threads disguised as treatment.</p>",
     "org-hero-recovery.png", True)
page("recovery/logistics", "Recovery logistics", "Practical tools for appointments, reminders, and daily structure.",
     "<p>Calendars, checklists, and transport notes. Support tools, not clinical care plans.</p>",
     "org-hero-recovery.png", True)
page("recovery/stories", "Recovery stories", "Consented lived experience writing.",
     "<p>Stories publish only with clear consent and review. Readers can leave anytime.</p>",
     "org-hero-recovery.png", True)
page("recovery/resources", "Recovery resources", "Curated external and local Edmonton resources.",
     "<p>Directories change. Verify before you go. We list; we do not endorse medical providers as treatment.</p>",
     "org-hero-recovery.png", True)

page("parkinsons", "Parkinsons support education", "Education, caregiver logistics, routines, and community. Not diagnosis or treatment.",
     """
     <ul>
       <li><a href="../parkinsons/education/">Plain language living well education</a></li>
       <li><a href="../parkinsons/tools/">Journaling and caregiver logistics tools</a></li>
       <li><a href="../parkinsons/community/">Family and caregiver discussion</a></li>
       <li><a href="../parkinsons/resources/">Curated external resources</a></li>
       <li><a href="../parkinsons/caregivers/">Caregiver guides</a></li>
       <li><a href="../parkinsons/routines/">Routine journaling templates</a></li>
     </ul>
     """,
     "org-hero-parkinsons.png", True)
page("parkinsons/education", "Parkinsons education", "Plain language education pages for families.", "<p>Educational framing only. Talk to qualified clinicians for care decisions.</p>", "org-hero-parkinsons.png", True)
page("parkinsons/tools", "Parkinsons tools", "Journaling and logistics helpers.", "<p>Track routines and notes privately. Not a medical device.</p>", "org-hero-parkinsons.png", True)
page("parkinsons/community", "Parkinsons community", "Family and caregiver discussion spaces.", "<p>Moderated. Kindness required. No treatment advice posing as clinical guidance.</p>", "org-hero-parkinsons.png", True)
page("parkinsons/resources", "Parkinsons resources", "External links and local pointers.", "<p>Verify every link. Organizations change.</p>", "org-hero-parkinsons.png", True)
page("parkinsons/caregivers", "Caregiver guides", "Practical caregiver oriented education.", "<p>Support for the people who support. Still not clinical advice.</p>", "org-hero-parkinsons.png", True)
page("parkinsons/routines", "Routines", "Routine journaling templates.", "<p>Morning, meds reminder logs as personal notes only, evening wind down.</p>", "org-hero-parkinsons.png", True)

page("eco-earn", "Eco-Earn", "Recycling and reuse gamification for cities, schools, brands, and households.",
     """
     <ul>
       <li><a href="../eco-earn/how/">How points and rewards work</a></li>
       <li><a href="../eco-earn/map/">Local partner and drop off map</a></li>
       <li><a href="../eco-earn/schools/">School and classroom challenges</a></li>
       <li><a href="../eco-earn/partners/">Municipal and brand partner portal</a></li>
       <li><a href="../eco-earn/leaderboards/">Local challenges and leaderboards</a></li>
       <li><a href="../eco-earn/kits/">Starter kits and physical bins or tags</a></li>
     </ul>
     """,
     "org-hero-eco-earn.png")
page("eco-earn/how", "How Eco-Earn works", "Points, challenges, and rewards explained.", "<p>Earn for verified recycling and reuse actions. Sponsors fund rewards. Privacy respecting by default.</p>", "org-hero-eco-earn.png")
page("eco-earn/map", "Eco-Earn map", "Drop off and partner map concept.", "<p>Map soft launches with Edmonton first, then expands.</p>", "org-hero-eco-earn.png")
page("eco-earn/schools", "Eco-Earn schools", "Classroom challenge kits.", "<p>Teachers get challenge packs. Students earn collective points for school rewards.</p>", "org-hero-eco-earn.png")
page("eco-earn/partners", "Eco-Earn partners", "City and brand partner intake.", "<p>Interest form: email partners with subject Eco-Earn partner.</p>", "org-hero-eco-earn.png")
page("eco-earn/leaderboards", "Leaderboards", "Local challenges and friendly competition.", "<p>Opt in leaderboards. No shaming mechanics.</p>", "org-hero-eco-earn.png")
page("eco-earn/kits", "Eco-Earn kits", "Physical starter kits, bins, and tags.", "<p>Household and school kits that plug into the digital loop.</p>", "org-hero-eco-earn.png")

page("books", "Books", "Phyllux Tech publishing and Sproule Lit. Primers, journals, fiction, education booklets.",
     """
     <p>Browse and buy on <a href="https://phyllux.com">phyllux.com</a> (Sproule Lit storefront). This page is the mission bridge.</p>
     <ul>
       <li>Quantonics primers and MoQ practical journals</li>
       <li>Recovery support practical guides (non clinical)</li>
       <li>Parkinsons family education series (education only)</li>
       <li>Eco-Earn handbooks</li>
       <li>Uncertainty and decision field guides</li>
       <li>Youth exploration and educator classroom guides</li>
       <li>Novelmate fiction lines under Sproule Lit pen names</li>
     </ul>
     <p><a href="../books/free/">Free primers</a> · <a href="../academy/">Academy courses</a></p>
     """,
     "org-hero-books.png")
page("books/free", "Free primers", "Free introductory reads.", "<p>Free primers lower the door. Paid full books stay on phyllux.com.</p>", "org-hero-books.png")

page("apps", "Apps", "Quantonics ships as Quanton Suite on phyllux.app. One mega app. Modules inside it.",
     """
     <p>Public product home: <a href="https://phyllux.app">phyllux.app</a>.</p>
     <ul>
       <li><a href="https://phyllux.app/suite/">Quanton Suite</a> is the product</li>
       <li>Module map lives inside Suite</li>
       <li>Desktop and iPhone parity later from the same core</li>
       <li><a href="https://phyllux.app/ecosystem/">Ecosystem map</a> for the wider Phyllux Tech circle</li>
     </ul>
     """,
     "org-hero-apps.png")
page("suite", "Quanton Suite", "One mega app hosting Quantonics modules with a category launcher.",
     "<p>Shared Quanton core. Feature flags. One Suite, not a mall of singles. Soft launch and waitlist via <a href=\"https://phyllux.app/suite/\">phyllux.app/suite</a>.</p>", "org-hero-apps.png")
page("marketplace", "Marketplace", "Gateway into Quanton Suite on phyllux.app.",
     "<p>Discovery and bundles point at <a href=\"https://phyllux.app/suite/\">Quanton Suite</a>. One Suite product, not a mall of singles.</p>", "org-hero-apps.png")

page("lab", "Lab", "3D printing, rapid prototyping, CAD, and maker education.",
     """
     <ul>
       <li><a href="../lab/3d/">3D print booking</a></li>
       <li>CAD and product design studio</li>
       <li>Rapid prototyping and light assembly</li>
       <li>3D scan and reverse engineering services</li>
       <li>Maker education workshops</li>
     </ul>
     <p>Interest: use <a href="../contact/">contact</a> with subject Lab.</p>
     """,
     "org-hero-lab.png")
page("lab/3d", "3D print", "Short run FDM and resin printing.", "<p>Parts, fixtures, prototypes. Edmonton first with ship options.</p>", "org-hero-lab.png")

page("studio", "Studio", "Recording studio installs, acoustic design, mixing, mastering, podcast production.",
     """
     <ul>
       <li>Turnkey studio design and install</li>
       <li>Acoustic measurement and treatment plans</li>
       <li>Remote and in person mix / master</li>
       <li>Podcast production</li>
       <li>Ongoing support contracts for installed systems</li>
     </ul>
     """,
     "org-hero-studio.png")

page("vst", "VST Audio", "Plugin creation and sales, samples, licensing.",
     """
     <ul>
       <li>VST factory catalog</li>
       <li>Sample and loop packs</li>
       <li>Audio plugin licensing to other companies</li>
       <li>Quantonic soundscape packs</li>
     </ul>
     """,
     "org-hero-vst.png")

page("build-it", "Build and IT", "Custom PCs, repair, networking, web design, game design, IT staffing.",
     """
     <ul>
       <li>Custom desktops and AI workstations</li>
       <li>NAS / home server builds and network setup</li>
       <li>Website agency and care plans</li>
       <li>Accessibility and performance audits</li>
       <li>Game studio and contract games</li>
       <li>IT staffing and fractional IT</li>
       <li>Local first edge appliances</li>
     </ul>
     """,
     "org-hero-build-it.png")

page("institutions", "Institutions", "Admin and education tooling for schools, government, business, and hospital administration.",
     """
     <ul>
       <li><a href="../schools/">Schools</a> AI literacy and knowledge ops</li>
       <li><a href="../government/">Government</a> municipal knowledge tools</li>
       <li><a href="../business/">Business</a> decision and uncertainty tooling</li>
       <li><a href="../hospital-admin/">Hospital admin</a> ops and training literacy only</li>
     </ul>
     <p class="disclaimer">No clinical diagnostic devices. No medical treatment claims.</p>
     """,
     "org-hero-institutions.png")
page("schools", "Schools", "AI literacy, knowledge systems, STEM uncertainty kits, site licenses.",
     "<p>Teacher dashboards, debate simulators, classroom kits. Education seats available.</p>", "org-hero-institutions.png")
page("government", "Government", "Municipal and public sector knowledge ops.",
     "<p>Non partisan admin tooling. Deliberation facilitation. Staff training packs.</p>", "org-hero-institutions.png")
page("business", "Business", "SMB uncertainty, scenario, and decision support.",
     "<p>Assumption trackers, scenario generators, quality decision matrices as B2B seats.</p>", "org-hero-institutions.png")
page("hospital-admin", "Hospital admin", "Scheduling literacy, document ops training, knowledge base tools for admin staff.",
     "<p class=\"disclaimer\">Administration and training only. Not a medical device. Not for diagnosis or treatment.</p>", "org-hero-institutions.png", True)

page("community", "Community", "Forums, events, Chautauqua, workshops, volunteer.",
     """
     <ul>
       <li><a href="../chautauqua/">Chautauqua and gatherings</a></li>
       <li><a href="../events/">Events calendar</a></li>
       <li><a href="../workshops/">Workshops</a></li>
       <li><a href="../volunteer/">Volunteer roles</a></li>
       <li><a href="../newsletter/">Newsletter</a></li>
     </ul>
     """,
     "org-hero-community.png")
page("chautauqua", "Chautauqua", "Events and gatherings in the Quantonics / Phyllux Tech spirit.", "<p>Tickets and sponsors. Edmonton first.</p>", "org-hero-community.png")
page("events", "Events", "Calendar of workshops and meetups.", "<p>Public calendar soft launches with the first workshop slate.</p>", "org-hero-community.png")
page("workshops", "Workshops", "Paid introductions and applied workshops.", "<p>Quantonics literacy, Eco-Earn, maker lab, studio craft.</p>", "org-hero-community.png")
page("volunteer", "Volunteer", "Volunteer roles across missions.", "<p>Community moderation, event help, Eco-Earn outreach.</p>", "org-hero-community.png")
page("newsletter", "Newsletter", "Subscribe for mission updates.", "<p>Low volume. Unsubscribe anytime. No spam.</p>", "org-hero-community.png")

page("academy", "Academy", "Courses, paths, and certificates.",
     "<p>Quantonics 101, QELR, MoQ literacy, AI ops literacy for institutions. Certification path later.</p>", "org-hero-academy.png")
page("labs", "Public labs", "Public experiments and open notes.", "<p>Research notes, prototypes, and open experiments that are safe to share.</p>", "org-hero-lab.png")
page("research", "Research", "Open research notes (non clinical).", "<p>Pointers into Quantonics catalog and literature tools.</p>", "org-hero-apps.png")
page("tools/journal", "Browser journal", "Browser journal prototypes.", "<p>Lightweight prototypes before app installs.</p>", "org-hero-recovery.png", True)
page("tools/decision", "Decision tools", "Perspective and decision exercises.", "<p>Uncertainty aware decision drills.</p>", "org-hero-apps.png")
page("tools/value-map", "Value map", "Personal value mapping exercises.", "<p>MoQ flavored personal mapping, not therapy.</p>", "org-hero-apps.png")

page("quantonics", "Quantonics", "Catalog explainers and speculative design framing.",
     "<p>Quantonics is philosophical and speculative. Software design source, not a physics proof. See also <a href=\"../qelr/\">QELR</a> and <a href=\"../moq/\">MoQ</a>.</p>", "org-hero-apps.png")
page("qelr", "QELR", "QELR literacy and language tools bridge.", "<p>Translator, dictionary, vocabulary trainer concepts live in the app catalog.</p>", "org-hero-apps.png")
page("moq", "MoQ", "Metaphysics of Quality introduction.", "<p>Practical journals and literacy paths. Bridge to books and academy.</p>", "org-hero-books.png")
page("novelmate", "Novelmate", "Bridge to Novelmate Studio.", "<p>Local first manuscript craft. <a href=\"https://novelmatestudio.com\">novelmatestudio.com</a></p>", "org-hero-books.png")
page("finally-me", "Finally Me", "Bridge to finallyme.help recovery methodology lane.",
     "<p>Paul Chartier methodology with David. Open beta at <a href=\"https://finallyme.help\">finallyme.help</a>. Not treatment.</p>", "org-hero-recovery.png", True)
page("today", "Today", "Local first recovery notebook. Live page on phyllux.com.", "<p>Open the working surface on <a href=\"https://phyllux.com/today.html\">phyllux.com/today</a>. No account. Notes on device. Still being built. Not on Play Store yet.</p>", "org-hero-recovery.png", True)

page("merch", "Merch", "Apparel, prints, symbol goods, subscription boxes.",
     "<p>Merch and monthly prompt tool boxes soft launch after brand pack is locked.</p>", "org-hero-merch.png")
page("donate", "Donate", "Support the missions.", "<p>Donations and sponsorships fund recovery education, Eco-Earn pilots, and open tools.</p>", "org-hero-donate.png")
page("sponsors", "Sponsors", "Sponsor and foundation information.", "<p>Eco-Earn, education kits, and community events welcome sponsors.</p>", "org-hero-partners.png")
page("partners", "Partners", "Paul / Mattys Place / allies.", "<p>Partnership prospectus and ally list. Contact to collaborate.</p>", "org-hero-partners.png")
page("about", "About", "Story, Edmonton base, team.",
     "<p>David E. Sproule · Edmonton, Alberta. Phyllux Technologies. Co founder work with Paul Chartier on client lanes. Local first. Honest research. Pattern grounded technology.</p>", "org-hero-edmonton.png")
page("contact", "Contact", "Contact and partnership form.",
     """
     <p>Email <a href="mailto:hello@phyllux.org">hello@phyllux.org</a> (forward to be wired) or use your existing Phyllux Tech contact channel.</p>
     <p>Useful subjects: Suite waitlist · Eco-Earn partner · Lab booking · Studio install · School pilot · Press</p>
     """,
     "org-hero-home.png")
page("privacy", "Privacy", "Local first privacy position.",
     "<p>Prefer on device data. Optional sync behind interfaces. No required cloud to use core tools. See also <a href=\"../security/\">security</a>.</p>", "org-hero-privacy.png")
page("security", "Security", "Security and data handling.", "<p>Encryption at rest for personal journals where claimed. Responsible disclosure welcome.</p>", "org-hero-privacy.png")
page("terms", "Terms", "Terms of use.", "<p>Draft terms for soft launch. Full counsel review before paid products.</p>", "org-hero-home.png")
page("legal", "Legal", "Legal notices and disclaimers.",
     """
     <p class="disclaimer">Recovery, Parkinsons, and wellness lanes are education, community, journaling, and logistics. Not medical advice, diagnosis, therapy, or treatment.</p>
     <p class="disclaimer">Hospital admin materials are for administration, scheduling literacy, and training content only. Not clinical devices.</p>
     <p class="disclaimer">Quantonics material is philosophical and speculative design framing, not a claim of scientific validation as physics.</p>
     """,
     "org-hero-home.png", True)
page("accessibility", "Accessibility", "Accessibility commitments.", "<p>Aim for WCAG minded pages. Report barriers via contact.</p>", "org-hero-home.png")
page("press", "Press", "Media kit.", "<p>Logos, mission one pager, and founder bio pack coming. Contact for now.</p>", "org-hero-home.png")
page("careers", "Careers", "Open roles.",
     "<p>Android builders, web designers, mix/master engineers, CAD/3D techs, IT/PC techs, community support (non clinical). See hire plan in the Paul brief.</p>", "org-hero-careers.png")
page("roadmap", "Roadmap", "Public high level roadmap.",
     """
     <ol>
       <li>Q1: Phase 0 foundations, phyllux.app live, this site live, Eco-Earn concept, book list freeze</li>
       <li>Q2: First Android ship slice, lab soft booking, PC soft launch, hire Android + web</li>
       <li>Q3: Quanton Suite soft launch proof, studio jobs, VST prototype, recovery pages live</li>
       <li>Q4–Q12: category waves, institutional pilots, Eco-Earn city talks, scale hiring</li>
       <li>Y4–Y5: full catalog strategy, geographic expansion, API/SDK</li>
     </ol>
     """,
     "org-hero-roadmap.png")
page("impact", "Impact", "Community and eco impact stories.", "<p>Publish measured stories as pilots complete. No vanity metrics.</p>", "org-hero-eco-earn.png")
page("edmonton", "Edmonton", "Local Edmonton programs and meetups.",
     "<p>Home base. Local Eco-Earn, workshops, studio, and PC shop soft launches start here.</p>", "org-hero-edmonton.png")
page("blog", "Blog", "Articles and updates.", "<p>Mission updates, build logs, and education posts.</p>", "org-hero-home.png")
page("faq", "FAQ", "Cross mission FAQ.", "<p>Common questions on apps, books, recovery education, Eco-Earn, and hiring.</p>", "org-hero-home.png")
page("glossary", "Glossary", "Terms and concepts.", "<p>Quanton, QELR, MoQ, Eco-Earn, Quanton Suite, module, local first.</p>", "org-hero-apps.png")
page("open-source", "Open source", "Open components and contribute.", "<p>Core pieces may dual license. Sponsorship welcome.</p>", "org-hero-apps.png")
page("podcast", "Podcast", "Podcast lane.", "<p>Own show plus client podcast production via Studio.</p>", "org-hero-studio.png")
page("shop", "Shop", "Merch and kits shop bridge.", "<p>Points to merch and Eco-Earn kits when inventory is ready.</p>", "org-hero-merch.png")
page("hire", "Hire", "Careers alias.", "<p>See <a href=\"../careers/\">careers</a>.</p>", "org-hero-careers.png")
page("it", "IT services", "IT services alias into Build and IT.", "<p>See <a href=\"../build-it/\">Build and IT</a>.</p>", "org-hero-build-it.png")
page("web", "Web design", "Website agency intake.", "<p>SMB sites, care plans, accessibility. Contact with subject Web.</p>", "org-hero-build-it.png")
page("games", "Games", "Game design lane.", "<p>First party Phyllux Tech / Quantonics games and client contracts.</p>", "org-hero-apps.png")
page("pcs", "PCs", "Custom PC shop.", "<p>Creator and AI workstation builds. See Build and IT.</p>", "org-hero-build-it.png")
page("image-gallery", "Image gallery", "Visual mission wall.",
     """
     <div class="gallery">
       <figure><img src="../assets/org-hero-home.png" alt="Home"/><figcaption>Home</figcaption></figure>
       <figure><img src="../assets/org-hero-recovery.png" alt="Recovery"/><figcaption>Recovery</figcaption></figure>
       <figure><img src="../assets/org-hero-parkinsons.png" alt="Parkinsons"/><figcaption>Parkinsons support education</figcaption></figure>
       <figure><img src="../assets/org-hero-eco-earn.png" alt="Eco-Earn"/><figcaption>Eco-Earn</figcaption></figure>
       <figure><img src="../assets/org-hero-books.png" alt="Books"/><figcaption>Books</figcaption></figure>
       <figure><img src="../assets/org-hero-apps.png" alt="Apps"/><figcaption>Apps</figcaption></figure>
       <figure><img src="../assets/org-hero-lab.png" alt="Lab"/><figcaption>Lab</figcaption></figure>
       <figure><img src="../assets/org-hero-studio.png" alt="Studio"/><figcaption>Studio</figcaption></figure>
       <figure><img src="../assets/org-hero-institutions.png" alt="Institutions"/><figcaption>Institutions</figcaption></figure>
       <figure><img src="../assets/org-hero-community.png" alt="Community"/><figcaption>Community</figcaption></figure>
       <figure><img src="../assets/org-hero-build-it.png" alt="Build"/><figcaption>Build and IT</figcaption></figure>
       <figure><img src="../assets/org-hero-vst.png" alt="VST"/><figcaption>VST</figcaption></figure>
       <figure><img src="../assets/org-hero-roadmap.png" alt="Roadmap"/><figcaption>Roadmap</figcaption></figure>
       <figure><img src="../assets/org-hero-privacy.png" alt="Privacy"/><figcaption>Privacy</figcaption></figure>
       <figure><img src="../assets/org-hero-careers.png" alt="Careers"/><figcaption>Careers</figcaption></figure>
       <figure><img src="../assets/org-hero-edmonton.png" alt="Edmonton"/><figcaption>Edmonton</figcaption></figure>
     </div>
     """,
     "org-hero-home.png")


NAV = [
    ("/", "Home"),
    ("/recovery/", "Recovery"),
    ("/parkinsons/", "Parkinsons"),
    ("/eco-earn/", "Eco-Earn"),
    ("/books/", "Books"),
    ("/apps/", "Apps"),
    ("/lab/", "Lab"),
    ("/studio/", "Studio"),
    ("/institutions/", "Institutions"),
    ("/roadmap/", "Roadmap"),
    ("/contact/", "Contact"),
]


CSS_TEXT = r"""
:root {
  --ink: #14212b;
  --muted: #4a5d6a;
  --paper: #f7f3ea;
  --card: #fffdf8;
  --teal: #0f6b6d;
  --teal-deep: #0a4547;
  --gold: #c4a35a;
  --line: #d9d0c0;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: "Source Sans 3", "Segoe UI", sans-serif;
  color: var(--ink);
  background:
    radial-gradient(1100px 520px at 8% -10%, #dceeee 0%, transparent 55%),
    radial-gradient(900px 480px at 100% 0%, #f0e6c8 0%, transparent 50%),
    var(--paper);
  line-height: 1.55;
}
a { color: var(--teal); }
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 1.15rem 3.5rem; }
.site-header {
  position: sticky; top: 0; z-index: 20;
  backdrop-filter: blur(10px);
  background: rgba(247,243,234,.9);
  border-bottom: 1px solid var(--line);
}
.header-inner { max-width: 1080px; margin: 0 auto; padding: .75rem 1.15rem; display: flex; gap: 1rem; align-items: center; justify-content: space-between; flex-wrap: wrap; }
.brand { font-family: Fraunces, Georgia, serif; font-weight: 700; font-size: 1.35rem; color: var(--teal-deep); text-decoration: none; }
.nav { display: flex; flex-wrap: wrap; gap: .55rem .85rem; }
.nav a { text-decoration: none; color: var(--muted); font-size: .92rem; font-weight: 600; }
.nav a:hover { color: var(--teal); }
.hero { margin: 1.2rem 0 1.5rem; border-radius: 18px; overflow: hidden; box-shadow: 0 18px 40px rgba(20,33,43,.16); position: relative; }
.hero img { width: 100%; display: block; max-height: 420px; object-fit: cover; }
.hero-caption {
  position: absolute; left: 1rem; bottom: 1rem;
  background: rgba(10,69,71,.88); color: #fff; padding: .55rem .9rem; border-radius: 999px; font-weight: 600;
}
h1,h2,h3 { font-family: Fraunces, Georgia, serif; color: var(--teal-deep); line-height: 1.15; }
h1 { font-size: clamp(2rem, 4.5vw, 3.1rem); margin: .4rem 0; }
h2 { font-size: 1.45rem; margin: 1.8rem 0 .55rem; }
.lede { font-size: 1.15rem; color: var(--muted); max-width: 54ch; }
.disclaimer, .note { color: var(--muted); font-size: .92rem; }
.disclaimer {
  background: #fff6e8; border: 1px solid var(--gold); border-radius: 12px; padding: .85rem 1rem; margin: 1rem 0;
}
.tile-grid, .gallery {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: .9rem; margin: 1.2rem 0;
}
.tile, .gallery figure {
  background: var(--card); border: 1px solid var(--line); border-radius: 16px; overflow: hidden; text-decoration: none; color: inherit;
  box-shadow: 0 8px 20px rgba(20,33,43,.06);
}
.tile img, .gallery img { width: 100%; height: 130px; object-fit: cover; display: block; }
.tile span, .gallery figcaption { display: block; padding: .65rem .8rem .2rem; font-weight: 700; color: var(--teal-deep); }
.tile em { display: block; padding: 0 .8rem .8rem; font-style: normal; color: var(--muted); font-size: .9rem; }
.site-footer {
  margin-top: 3rem; padding: 1.4rem 0 2rem; border-top: 1px solid var(--line); color: var(--muted); font-size: .9rem;
}
.footer-links { display: flex; flex-wrap: wrap; gap: .5rem .9rem; margin: .6rem 0 1rem; }
ul { padding-left: 1.15rem; }
li { margin: .35rem 0; }
@media (max-width: 720px) {
  .hero-caption { position: static; display: inline-block; margin: .6rem 0 0; }
}
"""


def rel_prefix(slug: str) -> str:
    if slug == "index":
        return ""
    depth = slug.count("/") + 1
    return "../" * depth


def asset_path(slug: str, filename: str) -> str:
    return f"{rel_prefix(slug)}assets/{filename}"


def css_path(slug: str) -> str:
    return f"{rel_prefix(slug)}css/site.css"


def href_for(slug: str, target: str) -> str:
    # target like /recovery/ or /
    t = target.strip("/")
    if not t:
        return "./" if slug == "index" else rel_prefix(slug)
    if slug == "index":
        return f"{t}/"
    return f"{rel_prefix(slug)}{t}/"


def render(page_data: dict) -> str:
    slug = page_data["slug"]
    prefix = rel_prefix(slug)
    nav = "".join(
        f'<a href="{href_for(slug, path)}">{label}</a>' for path, label in NAV
    )
    hero = ""
    if page_data.get("hero"):
        hero = f'''
  <div class="hero">
    <img src="{asset_path(slug, page_data['hero'])}" alt="{page_data['title']}"/>
    <div class="hero-caption">{page_data['title']}</div>
  </div>'''
    medical = ""
    if page_data.get("medical"):
        medical = '''
  <p class="disclaimer">Education, community, journaling, and logistics only. Not medical advice, diagnosis, therapy, or treatment. Not a clinical device.</p>'''
    # Fix home tile paths - they use recovery/ etc relative to root which is correct for index
    body = page_data["body"]
    if slug != "index":
        # gallery and similar already use ../assets
        pass
    home_href = "./" if slug == "index" else prefix
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{page_data['title']} · Phyllux.org</title>
<meta name="description" content="{page_data['lede'][:160]}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="{css_path(slug)}"/>
</head>
<body>
<header class="site-header"><div class="header-inner">
  <a class="brand" href="{home_href}">Phyllux Tech</a>
  <nav class="nav">{nav}</nav>
</div></header>
<main class="wrap">
{hero}
  <p class="note">{page_data['section']}</p>
  <h1>{page_data['title']}</h1>
  <p class="lede">{page_data['lede']}</p>
{medical}
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <div class="footer-links">
    <a href="https://phyllux.app/suite/">Quanton Suite</a>
    <a href="https://phyllux.app">phyllux.app</a>
    <a href="https://phyllux.com">phyllux.com books</a>
    <a href="https://phyllux.io">phyllux.io</a>
    <a href="https://novelmatestudio.com">Novelmate</a>
    <a href="https://finallyme.help">finallyme.help</a>
    <a href="{href_for(slug, '/legal/')}">Legal</a>
    <a href="{href_for(slug, '/privacy/')}">Privacy</a>
    <a href="{href_for(slug, '/contact/')}">Contact</a>
    <a href="{href_for(slug, '/image-gallery/')}">Gallery</a>
  </div>
  <p>Phyllux.org mission hub · David E. Sproule · Edmonton · Soft launch build 2026-09-14</p>
</div></footer>
</body>
</html>
"""


def copy_images() -> list[str]:
    STAGING.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    names = [
        "org-hero-home.png",
        "org-hero-recovery.png",
        "org-hero-parkinsons.png",
        "org-hero-eco-earn.png",
        "org-hero-books.png",
        "org-hero-apps.png",
        "org-hero-lab.png",
        "org-hero-studio.png",
        "org-hero-institutions.png",
        "org-hero-community.png",
        "org-hero-build-it.png",
        "org-hero-vst.png",
        "org-hero-roadmap.png",
        "org-hero-privacy.png",
        "org-hero-careers.png",
        "org-hero-edmonton.png",
        "org-hero-academy.png",
        "org-hero-merch.png",
        "org-hero-partners.png",
        "org-hero-donate.png",
        "org-tile-quanton.png",
        "org-tile-eco.png",
        "org-tile-recovery.png",
    ]
    # also pull useful pitch venture images as extras
    extras = [
        "paul-venture-merch.png",
        "paul-venture-subscription-box.png",
        "paul-venture-edge-appliance.png",
        "paul-venture-eco-earn-schools.png",
        "paul-venture-demo-booth.png",
        "paul-phyllux-org-missions.png",
    ]
    copied = []
    for n in names + extras:
        src = CURSOR_ASSETS / n
        if not src.exists():
            src = PITCH_ASSETS / n
        if not src.exists():
            print("MISS", n)
            continue
        shutil.copy2(src, STAGING / n)
        shutil.copy2(src, ASSETS / n)
        copied.append(n)
    return copied


def write_page(page_data: dict) -> Path:
    slug = page_data["slug"]
    if slug == "index":
        path = ROOT / "index.html"
    else:
        path = ROOT / slug / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(page_data), encoding="utf-8")
    return path


def main() -> None:
    CSS.mkdir(parents=True, exist_ok=True)
    (CSS / "site.css").write_text(CSS_TEXT, encoding="utf-8")
    copied = copy_images()
    paths = [write_page(p) for p in PAGES]
    # sitemap
    urls = []
    for p in PAGES:
        slug = p["slug"]
        urls.append("/" if slug == "index" else f"/{slug}/")
    (ROOT / "sitemap.txt").write_text("\n".join(urls) + "\n", encoding="utf-8")
    (ROOT / "README.md").write_text(
        f"""# phyllux.org mission hub

Static site for Phyllux.org missions (Round 3 union). Soft launch build.

## Run locally

Open `index.html` or serve:

```powershell
cd D:\\WS\\programs\\Phyllux-repos\\phyllux-org
python -m http.server 8765
```

Then visit http://127.0.0.1:8765/

## Deploy note

Live `phyllux.org` currently serves Sproule Lit. Prefer:

1. Deploy this tree to a host, then point phyllux.org here **after** moving Sproule Lit fully to phyllux.com, or
2. Mount under a cutover plan with redirects from old literary URLs to phyllux.com

Do not wipe books without a cutover checklist.

## Counts

- Pages: {len(PAGES)}
- Images copied: {len(copied)}
""",
        encoding="utf-8",
    )
    print("pages", len(paths))
    print("images", len(copied))


if __name__ == "__main__":
    main()
