define r = Character('Rika', color="#aa0022")
define y = Character('You', color="#fff0f0")

label day0_start:
    # 1. Title Card
    scene black
    with fade
    
    show text "{size=60}{color=#fff}DAY ?: The Fractured Crimson{/size}" at truecenter
    with dissolve
    $ renpy.pause(3.0, hard=True)
    hide text with dissolve

    # 2. Nostalgic Flashback Intro (Static Black Screen for memory)
    "I still remember the smell of the summer rain from ten years ago."
    "I remember the hidden shrine boundary we stumbled into as kids, the sound of her crying, and the terrifying, beautiful crimson light that suddenly flared from her eyes."
    "That was the day she shared a piece of her soul with me just to keep her awakening power from crushing my chest."
    "After that day, they gave her the heavy spectacles. They told us to forget."

    # 3. Transition to Modern Tokyo (Ultra-slow panning skyline)
    scene bg city:
        zoom 2.2
        yanchor 0.35
        ypos 0.5
        xalign 0.0
        linear 60.0 xalign 1.0
    with fade

    "They forced us to live as ordinary high school students blending into the endless sea of uniforms crossing Shinjuku every morning."
    "But you can’t seal an anomaly forever."
    
    # 4. The Shibuya Incident
    "It happened during the evening rush hour at Shibuya Station."
    "The suffocating heat, the overwhelming noise of the crowd... and the hidden dynasty scouts closing in on her trailing path."
    "The pressure didn't just break her composure."
    "It broke the {b}seal{/b}."

    # 5. The Explosion (Screen Shake & Flash)
    stop music fadeout 1.0
    scene white with vpunch
    $ renpy.pause(0.2)
    
    scene black with fade
    
    "A single microscopic slip in her focus."
    "In a fraction of a second, her magic circuits flared violently. The reinforced glass of her spectacles shattered outward."
    "The air pressure dropped instantly. The concrete beneath her feet cracked like brittle ice, and a localized reality-distortion wave blew through the station, short-circuiting every electronic grid within a three-block radius."
    "By the time the smoke cleared, she was gone."
    "She didn't get captured by an enemy strike team. She fled into hiding, terrified of the radioactive magical signal she had just blasted across Tokyo's ley lines."
    "Terrified of what she might do to me."

    # 6. The Tethered Curse / MC's realization
    "Because the moment her seal shattered, the dormant anchor inside my own chest snapped wide open."
    
    # Camera centers on the city and holds still
    scene bg city:
        zoom 2.2
        yanchor 0.35
        ypos 0.5
        xalign 0.5 
    with dissolve

    "Right now, a phantom heat is burning through my veins, rapidly draining my life force."
    "Her volatile energy is bleeding directly into my soul through our childhood link. If her core collapses, or if a rival family forces her final awakening, the spiritual feedback will obliterate us both."
    "Every hidden dynasty in the city felt that pulse. They are already locking down the sectors, hunting her down like a prize."
    "But they don't know her like I do."
    "She isn't running to escape them; she is running to protect me from herself."
    
    "The countdown has started."
    "I have exactly three days to find my childhood friend in this concrete labyrinth."
    "I'm not just saving her from the city—I'm chasing my own survival, and the only girl who ever truly understood the monster hiding in the dark."

    # 7. Transition into Day 1 Investigation Gameplay Loop
    $ days_remaining = 3
    jump day1_investigation
    