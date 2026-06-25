EXERCISE_LIBRARY = {
    "Quad sets": {
        "purpose": "Quadriceps activation and knee extension control.",
        "dosage": "10 reps x 5-10 sec holds, 2-3 sets",
        "cue": "Tighten the thigh and press the back of the knee down without holding breath.",
        "progression": "Progress to SLR, SAQ, LAQ, and closed-chain strengthening when quad control improves."
    },
    "Straight leg raises": {
        "aliases": ["SLR", "Straight Leg Raise"],
        "purpose": "Improve hip flexor and quadriceps strength while maintaining knee extension.",
        "dosage": "2-3 sets x 10-15 reps",
        "cue": "Lock the knee first, then lift the leg without an extension lag.",
        "progression": "Add ankle weight only when no lag is present."
    },
    "Clamshells": {
        "purpose": "Gluteus medius/external rotator strengthening.",
        "dosage": "2-3 sets x 10-20 reps",
        "cue": "Keep hips stacked and avoid rolling backward.",
        "progression": "Add band resistance or progress to side stepping/monster walks."
    },
    "Bridges": {
        "purpose": "Gluteal, hamstring, and lumbopelvic strengthening.",
        "dosage": "2-3 sets x 10-15 reps",
        "cue": "Squeeze glutes and lift hips without arching low back.",
        "progression": "Progress to single-leg bridge or physioball bridge."
    },
    "Monster walks": {
        "purpose": "Hip abductor and external rotator endurance for dynamic knee/hip control.",
        "dosage": "2-4 passes x 10-20 feet",
        "cue": "Keep knees aligned over toes and maintain band tension.",
        "progression": "Increase band resistance or add lateral/diagonal patterns."
    },
    "Lateral band walks": {
        "purpose": "Glute med strengthening and frontal plane control.",
        "dosage": "2-4 passes x 10-20 feet",
        "cue": "Small controlled steps; do not let feet snap together.",
        "progression": "Increase band resistance or add squat position."
    },
    "Step-ups": {
        "purpose": "Functional lower-extremity strengthening and stair mechanics.",
        "dosage": "2-3 sets x 8-12 reps",
        "cue": "Drive through the whole foot and control knee alignment.",
        "progression": "Increase step height or add march/hold."
    },
    "Step-downs": {
        "purpose": "Eccentric quad and hip control for stairs and running mechanics.",
        "dosage": "2-3 sets x 6-10 reps",
        "cue": "Slow lower; keep knee from collapsing inward.",
        "progression": "Increase height when pain-free with good control."
    },
    "Heel raises": {
        "purpose": "Gastroc/soleus strengthening and push-off power.",
        "dosage": "2-3 sets x 10-15 reps",
        "cue": "Rise through big toe and control the lowering phase.",
        "progression": "Double-leg to single-leg; add eccentric loading as appropriate."
    },
    "Chin tucks": {
        "purpose": "Deep neck flexor activation and cervical posture control.",
        "dosage": "10-15 reps, 3-5 sec holds",
        "cue": "Slide the chin straight back like making a double chin; do not look down.",
        "progression": "Progress to supine holds or resistance band when tolerated."
    },
    "Rows": {
        "purpose": "Scapular retraction and periscapular strengthening.",
        "dosage": "2-3 sets x 10-15 reps",
        "cue": "Pull elbows back and squeeze shoulder blades without shrugging.",
        "progression": "Increase band resistance or progress to cable rows."
    },
    "Band ER": {
        "aliases": ["Theraband ER", "Resisted ER", "External rotation strengthening", "Band external rotation"],
        "purpose": "Rotator cuff external rotator strengthening.",
        "dosage": "2-3 sets x 10-15 reps",
        "cue": "Keep elbow at side with towel roll; rotate out without trunk rotation.",
        "progression": "Increase resistance or progress to ER at 90° when appropriate."
    },
    "Band IR": {
        "aliases": ["Theraband IR", "Resisted IR", "Internal rotation strengthening", "Band internal rotation"],
        "purpose": "Rotator cuff internal rotator strengthening.",
        "dosage": "2-3 sets x 10-15 reps",
        "cue": "Keep elbow at side with towel roll; rotate inward slowly.",
        "progression": "Increase resistance or progress to functional diagonals."
    },
    "Scapular retractions": {
        "purpose": "Improve posture and scapular control.",
        "dosage": "2-3 sets x 10-15 reps with 3-5 sec holds",
        "cue": "Gently squeeze shoulder blades down and back without shrugging.",
        "progression": "Progress to rows, prone I/T/Y, or banded scapular work."
    },
    "Wall slides": {
        "purpose": "Shoulder or knee ROM and controlled functional movement depending on protocol.",
        "dosage": "2-3 sets x 10-15 reps",
        "cue": "Move slowly and stay within pain-free range.",
        "progression": "Increase range or add light resistance only when cleared."
    },
    "Pendulums": {
        "purpose": "Gentle shoulder mobility and pain modulation.",
        "dosage": "1-2 minutes each direction",
        "cue": "Let the arm relax and use body movement, not shoulder muscle effort.",
        "progression": "Progress to PROM/AAROM per protocol."
    },
    "Single-leg balance": {
        "aliases": ["SLS", "Single leg balance"],
        "purpose": "Balance, proprioception, and single-limb control.",
        "dosage": "3-5 rounds x 20-45 sec",
        "cue": "Keep pelvis level and knee aligned over toes.",
        "progression": "Eyes closed, foam, ball toss, clock taps, or Y-balance."
    },
    "Ankle theraband": {
        "aliases": ["Theraband DF/PF", "Theraband inversion", "Theraband eversion", "4-way ankle Theraband"],
        "purpose": "Ankle strengthening in dorsiflexion, plantarflexion, inversion, and eversion.",
        "dosage": "2-3 sets x 10-20 reps each direction",
        "cue": "Move slowly through controlled range without compensating at the hip/knee.",
        "progression": "Increase band resistance or progress to closed-chain strengthening."
    }
}


def find_exercise_info(exercise_name: str):
    """Return exercise details if the protocol item matches a known exercise or alias."""
    if not exercise_name:
        return None
    text = exercise_name.lower()
    for name, details in EXERCISE_LIBRARY.items():
        terms = [name] + details.get("aliases", [])
        for term in terms:
            if term.lower() in text or text in term.lower():
                return name, details
    return None
