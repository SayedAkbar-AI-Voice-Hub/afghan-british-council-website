import os
import re

# Read template file (about.html)
with open('about.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Pages dict
pages = {
    'membership-tiers.html': '''    <header class="subpage-hero" style="background-image: linear-gradient(rgba(13,27,62,0.85), rgba(26,43,92,0.75)), url('3.jpg'); background-size: cover; background-position: center;">
        <div class="container relative z-10 text-center">
            <h1 class="gsap-fade-up">Membership Tiers &amp; Benefits</h1>
            <p class="gsap-fade-up" style="animation-delay: 0.2s; font-size: 1.2rem; color: rgba(255,255,255,0.85); max-width: 640px; margin: 1rem auto 0;">Find the right level of support for your personal and professional growth.</p>
        </div>
    </header>
    <section class="section">
        <div class="container">
            <div class="grid-3 text-center">
                <div class="glass-card gsap-stagger-item">
                    <h3 style="font-size: 1.8rem; margin-bottom: 0.5rem;">Free</h3>
                    <p style="font-size: 2.5rem; color: var(--accent); margin-bottom: 1rem; font-family: var(--font-serif);">£0</p>
                    <ul style="list-style: none; text-align: left; margin-bottom: 2rem;">
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check text-accent" style="margin-right: 10px;"></i> Access to our private WhatsApp community.</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check text-accent" style="margin-right: 10px;"></i> Basic networking opportunities.</li>
                    </ul>
                    <a href="get-involved.html" class="btn btn-outline-white" style="width: 100%;">Join Free</a>
                </div>
                <div class="glass-card gsap-stagger-item" style="border: 2px solid var(--accent); transform: scale(1.05);">
                    <div style="background: var(--accent); color: var(--dark); padding: 5px 0; margin: -2rem -2rem 1.5rem; font-weight: 600; border-radius: var(--radius-sm) var(--radius-sm) 0 0;">POPULAR</div>
                    <h3 style="font-size: 1.8rem; margin-bottom: 0.5rem;">Standard</h3>
                    <p style="font-size: 2.5rem; color: var(--accent); margin-bottom: 1rem; font-family: var(--font-serif);">£25<span style="font-size: 1rem; color: var(--gray);">/month</span></p>
                    <ul style="list-style: none; text-align: left; margin-bottom: 2rem;">
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check text-accent" style="margin-right: 10px;"></i> Access to all ABC networking events and cultural gatherings.</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check text-accent" style="margin-right: 10px;"></i> Full access to the online member platform and Knowledge Hub.</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check text-accent" style="margin-right: 10px;"></i> Exclusive community perks and partner discounts.</li>
                    </ul>
                    <a href="get-involved.html" class="btn btn-primary" style="width: 100%;">Get Standard</a>
                </div>
                <div class="glass-card gsap-stagger-item">
                    <h3 style="font-size: 1.8rem; margin-bottom: 0.5rem;">Premium Growth</h3>
                    <p style="font-size: 2.5rem; color: var(--accent); margin-bottom: 1rem; font-family: var(--font-serif);">£75<span style="font-size: 1rem; color: var(--gray);">/month</span></p>
                    <ul style="list-style: none; text-align: left; margin-bottom: 2rem;">
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-check text-accent" style="margin-right: 10px;"></i> Includes all Standard benefits</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-star text-accent" style="margin-right: 10px;"></i> Personalized business and career direction.</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-star text-accent" style="margin-right: 10px;"></i> 1-on-1 mentorship and growth pairing.</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-star text-accent" style="margin-right: 10px;"></i> Priority introductions to strategic partners and investors.</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-star text-accent" style="margin-right: 10px;"></i> Premium support resources and dedicated career guidance.</li>
                    </ul>
                    <a href="get-involved.html" class="btn btn-outline-white" style="width: 100%;">Get Premium</a>
                </div>
            </div>
        </div>
    </section>''',
    
    'event-management.html': '''    <header class="subpage-hero" style="background-image: linear-gradient(rgba(13,27,62,0.85), rgba(26,43,92,0.75)), url('4.jpg'); background-size: cover; background-position: center;">
        <div class="container relative z-10 text-center">
            <h1 class="gsap-fade-up">ABC Event Management &amp; Bookings</h1>
            <p class="gsap-fade-up" style="animation-delay: 0.2s; font-size: 1.2rem; color: rgba(255,255,255,0.85); max-width: 640px; margin: 1rem auto 0;">We make your events unforgettable while protecting your interests.</p>
        </div>
    </header>
    <section class="section">
        <div class="container">
            <div class="grid-2">
                <div class="gsap-fade-up">
                    <h2 style="font-size: 2.5rem; margin-bottom: 1.5rem;">Full Event Management</h2>
                    <p style="margin-bottom: 1rem;">ABC offers full event management for:</p>
                    <ul style="list-style: none; margin-bottom: 1.5rem;">
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-circle text-accent" style="font-size: 0.6rem; margin-right: 10px; vertical-align: middle;"></i> Corporate Sponsorships</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-circle text-accent" style="font-size: 0.6rem; margin-right: 10px; vertical-align: middle;"></i> Concerts &amp; Entertainment</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-circle text-accent" style="font-size: 0.6rem; margin-right: 10px; vertical-align: middle;"></i> Weddings &amp; Private Celebrations</li>
                        <li style="margin-bottom: 0.5rem;"><i class="fas fa-circle text-accent" style="font-size: 0.6rem; margin-right: 10px; vertical-align: middle;"></i> Cultural Events</li>
                    </ul>
                    <p>By booking through ABC, our members benefit from our strong negotiation power, ensuring you get the best rates, premium venue access, and an extra layer of protection for your contracts.</p>
                    <div style="margin-top: 2rem;">
                        <a href="get-involved.html" class="btn btn-primary">Enquire Now</a>
                    </div>
                </div>
                <div class="rounded-img gsap-scale-up">
                    <img src="ABC_22.jpg" alt="Event Management">
                </div>
            </div>
        </div>
    </section>''',

    'partners-venues.html': '''    <header class="subpage-hero" style="background-image: linear-gradient(rgba(13,27,62,0.85), rgba(26,43,92,0.75)), url('5.jpg'); background-size: cover; background-position: center;">
        <div class="container relative z-10 text-center">
            <h1 class="gsap-fade-up">Partners &amp; Venues</h1>
            <p class="gsap-fade-up" style="animation-delay: 0.2s; font-size: 1.2rem; color: rgba(255,255,255,0.85); max-width: 640px; margin: 1rem auto 0;">Our strategic partners and venue connections</p>
        </div>
    </header>
    <section class="section">
        <div class="container">
            <h2 class="text-center gsap-fade-up" style="font-size: 2.5rem; margin-bottom: 3rem;">Strategic Partners</h2>
            <div class="grid-3 text-center" style="gap: 2rem;">
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">B&P Hub</h3><p class="text-accent" style="font-size: 0.85rem;">Strategic Joint Event Partner</p></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Syva Health</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Anari</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">B&P Consultancy</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Upstairs at Langan’s</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">NHS</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Watandar.snap</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Forbes 30 Under 30</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">TEDx Community</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Afghan Development Academy (ADA)</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">The Heart of Europe</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">FML</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Kapabay</h3></div>
            </div>
            
            <h2 class="text-center gsap-fade-up" style="font-size: 2.5rem; margin: 4rem 0 3rem;">Notable Venue Partners</h2>
            <div class="grid-3 text-center" style="gap: 2rem;">
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Langan’s Mayfair</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Home House</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Home Grown</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Greenford Business Lounge</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Dirty Martini</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">145 Knightsbridge</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Gaucho Group</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Grand Connaught Rooms</h3></div>
                <div class="glass-card gsap-stagger-item"><h3 style="font-size: 1.3rem;">Old Sessions House</h3></div>
            </div>
        </div>
    </section>''',

    'ambassadors.html': '''    <header class="subpage-hero" style="background-image: linear-gradient(rgba(13,27,62,0.85), rgba(26,43,92,0.75)), url('6.jpg'); background-size: cover; background-position: center;">
        <div class="container relative z-10 text-center">
            <h1 class="gsap-fade-up">Ambassadors &amp; Notable Members</h1>
            <p class="gsap-fade-up" style="animation-delay: 0.2s; font-size: 1.2rem; color: rgba(255,255,255,0.85); max-width: 640px; margin: 1rem auto 0;">Highlighting high-profile individuals in our network.</p>
        </div>
    </header>
    <section class="section">
        <div class="container">
            <div class="grid-3 text-center" style="gap: 3rem 2rem;">
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--dark), var(--dark-light)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem; box-shadow: 0 8px 24px rgba(13,27,62,0.25);">QZ</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Quais Zulfat</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--accent), var(--accent-hover)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem; box-shadow: 0 8px 24px rgba(201,168,76,0.25);">RG</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Rahmanullah Gurbaz</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--dark), var(--dark-light)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem; box-shadow: 0 8px 24px rgba(13,27,62,0.25);">FD</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Farad Dayra</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--accent), var(--accent-hover)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem;">SA</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Surosh Azizi</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--dark), var(--dark-light)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem;">NK</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Nikolay Kirilov</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--accent), var(--accent-hover)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem;">AB</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Andrew Bryant</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--dark), var(--dark-light)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem;">CL</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Catriona Laing</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--accent), var(--accent-hover)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem;">MC</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Mina Chervenkova</h3>
                </div>
                <div class="gsap-stagger-item">
                    <div style="width: 150px; height: 150px; border-radius: 50%; background: linear-gradient(135deg, var(--dark), var(--dark-light)); color: white; display: flex; align-items: center; justify-content: center; font-family: var(--font-serif); font-size: 3rem; margin: 0 auto 1.5rem;">IH</div>
                    <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Inessa Harutunian</h3>
                </div>
            </div>
        </div>
    </section>''',

    'mentorship.html': '''    <header class="subpage-hero" style="background-image: linear-gradient(rgba(13,27,62,0.85), rgba(26,43,92,0.75)), url('1.jpg'); background-size: cover; background-position: center;">
        <div class="container relative z-10 text-center">
            <h1 class="gsap-fade-up">Mentorship &amp; Growth</h1>
            <p class="gsap-fade-up" style="animation-delay: 0.2s; font-size: 1.2rem; color: rgba(255,255,255,0.85); max-width: 640px; margin: 1rem auto 0;">We connect experienced professionals with ambitious starters. Share your skills, get guidance, and grow your career together.</p>
        </div>
    </header>''',

    'knowledge-hub.html': '''    <header class="subpage-hero" style="background-image: linear-gradient(rgba(13,27,62,0.85), rgba(26,43,92,0.75)), url('ABC_70.jpg'); background-size: cover; background-position: center;">
        <div class="container relative z-10 text-center">
            <h1 class="gsap-fade-up">Knowledge Hub</h1>
            <p class="gsap-fade-up" style="animation-delay: 0.2s; font-size: 1.2rem; color: rgba(255,255,255,0.85); max-width: 640px; margin: 1rem auto 0;">Access a library of resources. Find career toolkits, business guides, and educational materials to support your success in the UK.</p>
        </div>
    </header>''',

    'login.html': '''    <header class="subpage-hero" style="background-image: linear-gradient(rgba(13,27,62,0.85), rgba(26,43,92,0.75)), url('ABC_3.jpg'); background-size: cover; background-position: center; padding: 10rem 0 5rem;">
        <div class="container relative z-10 text-center">
            <h1 class="gsap-fade-up">Admin Portal</h1>
            <p class="gsap-fade-up" style="animation-delay: 0.2s; font-size: 1.2rem; color: rgba(255,255,255,0.85); max-width: 640px; margin: 1rem auto 0;">Login to Update Gallery and Upcoming Events</p>
        </div>
    </header>
    <section class="section">
        <div class="container">
            <div class="glass-card" style="max-width: 500px; margin: 0 auto;">
                <h3 class="text-center" style="font-size: 1.8rem; margin-bottom: 2rem;">Sign In</h3>
                <form id="login-form">
                    <div class="form-group">
                        <label class="form-label">Email</label>
                        <input type="email" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Password</label>
                        <input type="password" class="form-control" required>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">Sign In</button>
                    <p style="text-align: center; margin-top: 1rem; color: var(--gray); font-size: 0.9rem;">Authorised Access Only.</p>
                </form>
            </div>
        </div>
    </section>'''
}

for filename, content in pages.items():
    # Replace the middle part
    new_page_content = re.sub(r'<header class="subpage-hero".*?</section>.*?<!-- Use same footer -->\s*<footer class="footer">', content + '\n\n    <!-- Use same footer -->\n    <footer class="footer">', template, flags=re.DOTALL)
    # If the regex missed, it's probably because the end anchor is slightly different
    if "<!-- Use same footer -->" not in template:
        new_page_content = re.sub(r'<header class="subpage-hero".*?</section>.*?(?=\s*<footer class="footer">)', '\n' + content + '\n', template, flags=re.DOTALL)

    # Change the title tag
    title_text = filename.replace('.html', '').replace('-', ' ').title()
    new_page_content = re.sub(r'<title>.*?</title>', f'<title>{title_text} | Afghan British Council</title>', new_page_content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_page_content)

print(f"Created all extra pages.")
