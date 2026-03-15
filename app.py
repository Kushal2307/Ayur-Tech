from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        state = data.get('state', '')
        
        scores = {"Vata": 0, "Pitta": 0, "Kapha": 0}

        for i in range(1, 13):
            answer = data.get(f'q{i}')
            if answer == "V": scores["Vata"] += 1
            elif answer == "P": scores["Pitta"] += 1
            elif answer == "K": scores["Kapha"] += 1
            elif answer == "S": # Sama (Balanced)
                scores["Vata"] += 1
                scores["Pitta"] += 1
                scores["Kapha"] += 1

        total_score = sum(scores.values())
        if total_score == 0: total_score = 1
            
        percents = {
            "Vata": round((scores["Vata"] / total_score) * 100),
            "Pitta": round((scores["Pitta"] / total_score) * 100),
            "Kapha": round((scores["Kapha"] / total_score) * 100)
        }

        sorted_doshas = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        primary = sorted_doshas[0][0]
        secondary_en = sorted_doshas[1][0]
        
        hindi_map = {"Vata": "वात (Vata)", "Pitta": "पित्त (Pitta)", "Kapha": "कफ (Kapha)"}

        regional_advice = ""
        hot_states = ["Rajasthan", "Delhi", "Haryana", "Punjab", "Uttar Pradesh", "Gujarat"]
        humid_states = ["Maharashtra", "Kerala", "West Bengal", "Tamil Nadu", "Odisha", "Telangana"]
        cold_states = ["Himachal Pradesh", "Uttarakhand", "Jammu & Kashmir", "Sikkim"]

        if state in hot_states:
            regional_advice = "Extreme Climate Zone: Hydration and cooling herbs are crucial here. (गर्मी के मौसम में शरीर को ठंडा रखना आवश्यक है।)"
        elif state in humid_states:
            regional_advice = "Coastal/Humid Zone: Light, dry, and warm foods help balance energy. (तटीय/उमस वाले क्षेत्रों में हल्का और सुपाच्य भोजन लें।)"
        elif state in cold_states:
            regional_advice = "Cold/Hilly Zone: Warm, nourishing, and oily foods are essential. (पहाड़ी/ठंडे क्षेत्रों में गर्म और पौष्टिक आहार लें।)"
        else:
            regional_advice = "Moderate Zone: Follow the standard seasonal regime (Ritucharya). (सामान्य ऋतुचर्या का पालन करें।)"

        report = {
            "primary": hindi_map[primary],
            "secondary": hindi_map[secondary_en],
            "percentages": percents,
            "profile": "",
            "regional_advice": regional_advice,
            "dos": [],
            "donts": [],
            "herbs": "",
            "yoga_list": [],
            "routine": "",
            "sound_therapy": "", 
            "dosha_img": "",
            "yoga_img": "",
            "theme": {}
        }

        if primary == "Vata":
            report["profile"] = "You are naturally creative and energetic. Imbalance causes anxiety and dry skin. (आप स्वभाव से रचनात्मक हैं। संतुलन बिगड़ने पर चिंता की समस्या होती है।)"
            report["dos"] = ["गर्म और पौष्टिक भोजन करें (Eat warm, nourishing food).", "एक निश्चित दिनचर्या का पालन करें (Follow a strict daily routine)."]
            report["donts"] = ["ठंडी चीजें और कच्चा सलाद न खाएं (Strictly avoid raw salads).", "अत्यधिक मल्टीटास्किंग से बचें (Avoid extreme multitasking)."]
            report["herbs"] = "अश्वगंधा (Ashwagandha) & त्रिफला (Triphala)."
            report["yoga_list"] = ["बालासन (Child's Pose)", "वृक्षासन (Tree Pose)", "अनुलोम-विलोम (Anulom Vilom)"]
            report["routine"] = "सुबह 6 AM तक उठें। रात 10 PM तक सोना सर्वोत्तम है (Wake up by 6 AM, sleep by 10 PM)."
            report["sound_therapy"] = "432 Hz Frequency | Instruments: Flute (बांसुरी), Acoustic Guitar. (Helps ground the nervous system and reduce anxiety.)"
            
            # SECURE UNSPLASH LINKS
            report["dosha_img"] = "https://images.unsplash.com/photo-1518281420975-50db6e5d0a97?w=800&auto=format&fit=crop" 
            report["yoga_img"] = "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&auto=format&fit=crop" 
            
            report["theme"] = {"primary": "#8B4513", "bg": "linear-gradient(120deg, #f6d365 0%, #fda085 100%)"}

        elif primary == "Pitta":
            report["profile"] = "You are sharp, intelligent, and goal-oriented. Imbalance causes anger and acidity. (आप बुद्धिमान हैं। संतुलन बिगड़ने पर क्रोध और एसिडिटी होती है।)"
            report["dos"] = ["ठंडी तासीर वाला भोजन करें (Eat cooling foods like cucumber).", "प्रकृति के बीच समय बिताएं (Spend time in nature)."]
            report["donts"] = ["अधिक तीखा और तला हुआ भोजन न करें (Avoid spicy/fried foods).", "दोपहर की तेज धूप से बचें (Avoid strong afternoon sun)."]
            report["herbs"] = "आंवला (Amla) & ब्राह्मी (Brahmi)."
            report["yoga_list"] = ["भुजंगासन (Cobra Pose)", "चन्द्रासन (Moon Salutation)", "शीतली प्राणायाम (Sheetali Pranayama)"]
            report["routine"] = "सुबह 5:30 AM उठें। रात 10:30 PM तक सो जाएं (Wake up by 5:30 AM, sleep by 10:30 PM)."
            report["sound_therapy"] = "528 Hz Frequency | Instruments: Sitar (सितार), Water Sounds. (Cools down body heat and reduces anger/stress.)"
            
            # SECURE UNSPLASH LINKS
            report["dosha_img"] = "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop" 
            report["yoga_img"] = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=800&auto=format&fit=crop" 
            
            report["theme"] = {"primary": "#00695C", "bg": "linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%)"}
            
        else: # Kapha
            report["profile"] = "You are calm and possess a strong physical build. Imbalance causes lethargy and weight gain. (आप शांत स्वभाव के हैं। संतुलन बिगड़ने पर आलस्य और वजन बढ़ता है।)"
            report["dos"] = ["हल्का, गर्म और मसालेदार भोजन करें (Eat light, warm, spicy food).", "रोजाना तीव्र व्यायाम करें (Daily intense physical exercise)."]
            report["donts"] = ["भारी डेयरी उत्पाद से बचें (Avoid heavy dairy products).", "दिन में सोना बिल्कुल बंद करें (Strictly avoid daytime napping)."]
            report["herbs"] = "तुलसी (Tulsi) & अदरक (Ginger)."
            report["yoga_list"] = ["सूर्य नमस्कार (Surya Namaskar - Fast pace)", "वीरभद्रासन (Warrior Pose)", "कपालभाति (Kapalabhati)"]
            report["routine"] = "सुबह 5:00 AM उठें। रात 11:00 PM तक सो सकते हैं (Wake up by 5 AM, sleep by 11 PM)."
            report["sound_therapy"] = "396 Hz Frequency | Instruments: Tabla (तबला), Upbeat Drums. (Energizes the body and clears out lethargy/mucus.)"
            
            # SECURE UNSPLASH LINKS
            report["dosha_img"] = "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?w=800&auto=format&fit=crop" 
            report["yoga_img"] = "https://images.unsplash.com/photo-1575052814086-f385e2e2ad1b?w=800&auto=format&fit=crop" 
            
            report["theme"] = {"primary": "#B22222", "bg": "linear-gradient(120deg, #ff0844 0%, #ffb199 100%)"}

        return jsonify({"status": "success", "data": report})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5005)