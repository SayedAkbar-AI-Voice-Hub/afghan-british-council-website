import os
import re
import glob

nav_replacement = """            <ul class="nav-links">
                <li><a href="index.html" class="nav-link">Home</a></li>
                <li class="dropdown">
                    <a href="about.html" class="nav-link">About Us <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
                    <div class="dropdown-menu">
                        <a href="about.html#team" class="dropdown-item">The Team</a>
                        <a href="ambassadors.html" class="dropdown-item">Ambassadors & Notable Members</a>
                        <a href="partners-venues.html" class="dropdown-item">Partners & Venues</a>
                    </div>
                </li>
                <li class="dropdown">
                    <a href="#" class="nav-link">Activities & Services <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
                    <div class="dropdown-menu">
                        <a href="event-management.html" class="dropdown-item">Event Management</a>
                        <a href="#" class="dropdown-item">Education & Skills</a>
                        <a href="#" class="dropdown-item">Professional Networking</a>
                        <a href="#" class="dropdown-item">Social & Cultural Events</a>
                    </div>
                </li>
                <li class="dropdown">
                    <a href="#" class="nav-link">Resources <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
                    <div class="dropdown-menu">
                        <a href="mentorship.html" class="dropdown-item">Mentorship & Growth</a>
                        <a href="knowledge-hub.html" class="dropdown-item">Knowledge Hub</a>
                    </div>
                </li>
                <li class="dropdown">
                    <a href="membership-tiers.html" class="nav-link">Membership <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
                    <div class="dropdown-menu">
                        <a href="membership-tiers.html" class="dropdown-item">Membership Tiers & Benefits</a>
                    </div>
                </li>
                <li class="dropdown">
                    <a href="events.html" class="nav-link">Events & Media <i class="fas fa-chevron-down" style="font-size: 0.8em; margin-left: 5px;"></i></a>
                    <div class="dropdown-menu">
                        <a href="gallery.html" class="dropdown-item">Gallery</a>
                        <a href="#" class="dropdown-item">Podcast & Insights</a>
                    </div>
                </li>
            </ul>"""

social_replacement = """                    <div style="display: flex; gap: 1rem; margin-top: 1.5rem; flex-wrap: wrap; align-items: flex-start; max-width: 350px;">
                        <a href="https://www.facebook.com/share/1Awx9N39rG/" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><i class="fab fa-facebook" style="width: 20px;"></i> <span>Facebook</span></a>
                        <a href="https://x.com/AfghanBritishCo" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><span style="width: 20px; font-weight:700;">𝕏</span> <span>X (Twitter)</span></a>
                        <a href="https://www.instagram.com/afg_british_council" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><i class="fab fa-instagram" style="width: 20px;"></i> <span>Instagram</span></a>
                        <a href="https://www.twitch.tv/afghanbritishcouncil" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><i class="fab fa-twitch" style="width: 20px;"></i> <span>Twitch</span></a>
                        <a href="https://www.kick.com/afghanbritishcouncil" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; font-weight: 700; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><span style="width: 20px; font-size: 0.85em;">KICK</span> <span>Kick</span></a>
                        <a href="https://tiktok.com/@afghan.british.co" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><i class="fab fa-tiktok" style="width: 20px;"></i> <span>TikTok</span></a>
                        <a href="https://www.youtube.com/@AfghanBritishCouncilABC" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><i class="fab fa-youtube" style="width: 20px;"></i> <span>YouTube</span></a>
                        <a href="https://share.upscrolled.com/en/user/692a327b-0e41-47fe-a447-951884c621c1" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><i class="fas fa-scroll" style="width: 20px;"></i> <span>UpScrolled</span></a>
                        <a href="https://www.clubhouse.com/@hakimi.s" target="_blank" rel="noopener" style="color: rgba(255,255,255,0.6); text-decoration: none; display: flex; align-items: center; gap: 8px; width: 45%; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='rgba(255,255,255,0.6)'"><i class="fas fa-hand-peace" style="width: 20px;"></i> <span>Clubhouse</span></a>
                    </div>"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace the navigation links block
    content = re.sub(r'\s*<ul class="nav-links">.*?</ul>', '\n' + nav_replacement, content, flags=re.DOTALL)
    
    # Replace the social links block
    content = re.sub(r'\s*<div style="display: flex; gap: 1\.1rem; margin-top: 1\.5rem; flex-wrap: wrap; align-items: center;">.*?</div>', '\n' + social_replacement, content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Done updating HTMLs")
