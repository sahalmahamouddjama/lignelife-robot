import os
import requests
import json

# 🔑 CONFIGURATION DE VOS CLÉS GRATUITES (Prêtes pour le serveur en ligne)
GEMINI_API_KEY = "AQ.Ab8RN6LRDmWGdgL03NJJ45IjAv1KFHveEhfDTkYZHRW9y4OKNw"

JSONBIN_BIN_ID = "6a81a6edf5f4af5e291cba3f"
JSONBIN_API_KEY = "\$2a\$10\$ijBomvNp6abRYHZtUnNzvOig5ScKeTjcrPOIKKpJSDqMNMwIOGnYq"

def appeler_gemini_gratuit(prompt_text):
    # Adresse officielle et complète de Google Gemini
    url = f"https://googleapis.com{GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            res_json = response.json()
            return res_json["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            raise Exception("Erreur de lecture de la réponse de l'IA.")
    else:
        raise Exception(f"Erreur Google Gemini ({response.status_code}) : {response.text}")

def machine_a_contenu_automatique():
    print("🤖 ÉTAPE 1 : Écriture des 3 articles sur le Cloud (IA Gemini 100% Gratuite)...")
    theme_site = "Le Cloud Computing (Le Nuage), la sécurité du stockage réseau et la transformation digitale des entreprises."
    articles_bruts = []
    
    for i in range(1, 4):
        print(f"✍️ Rédaction de l'article {i}/3 par l'Outil 1...")
        prompt_redaction = (
            f"Écris un article de blog complet, professionnel et technique en FRANÇAIS sur le thème : {theme_site}. "
            f"Trouve un titre très accrocheur et différent pour cet article {i}. Utilise un ton d'expert."
        )
        try:
            texte_genere = appeler_gemini_gratuit(prompt_redaction)
            articles_bruts.append(texte_genere)
        except Exception as e:
            print(f"❌ Erreur lors de la génération : {e}")
            return

    print("\n🧠 ÉTAPE 2 : Humanisation anti-plagiat (Filtre Google AdSense)...")
    articles_humanises_valides = []
    
    for idx, contenu_robot in enumerate(articles_bruts):
        print(f"✨ L'Outil 2 transforme l'article {idx+1}/3 en style 100% humain...")
        
        prompt_humaniseur = (
            "Tu es un rédacteur humain professionnel. Réécris entièrement l'article fourni en respectant ces règles :\n"
            "1. Utilise un ton vivant, chaleureux et captivant.\n"
            "2. Varie fortement la longueur des phrases.\n"
            "3. N'utilise pas de listes à puces trop parfaites de robot.\n"
            "4. Reformule chaque paragraphe de façon unique pour garantir 0% de plagiat.\n"
            "Renvoie STRICTEMENT un format JSON sous cette forme exacte sans aucun autre texte autour, sans balises markdown ```json :\n"
            '{"title": "Titre humanisé", "category": "Cloud & Nuage", "content": "Le texte entièrement réécrit ici"}\n\n'
            f"Voici l'article à réécrire :\n{contenu_robot}"
        )
        
        try:
            reponse_humanisee = appeler_gemini_gratuit(prompt_humaniseur)
            reponse_humanisee = reponse_humanisee.replace("```json", "").replace("```", "").strip()
            
            article_propre = json.loads(reponse_humanisee)
            article_propre["image"] = ""
            articles_humanises_valides.append(article_propre)
        except Exception:
            articles_humanises_valides.append({
                "title": f"Découvrir le Nuage - Article {idx+1}",
                "category": "Cloud & Nuage",
                "content": contenu_robot[:1500],
                "image": ""
            })

    print("\n🌐 ÉTAPE 3 : Publication automatique sur votre site...")
    # Adresse officielle et complète de JSONBin
    url_cloud = f"https://jsonbin.io{JSONBIN_BIN_ID}"
    headers = {"X-Master-Key": JSONBIN_API_KEY}
    
    try:
        reponse_serveur = requests.get(f"{url_cloud}/latest", headers=headers)
        donnees_actuelles = reponse_serveur.json().get("record", {})
        liste_articles_existants = donnees_actuelles.get("articles", [])
        
        nouvelle_liste_totale = articles_humanises_valides + liste_articles_existants
        payload_mise_a_jour = {"articles": nouvelle_liste_totale}
        
        entetes_envoi = {"Content-Type": "application/json", "X-Master-Key": JSONBIN_API_KEY}
        mise_a_jour_serveur = requests.put(url_cloud, headers=entetes_envoi, data=json.dumps(payload_mise_a_jour))
        
        if mise_a_jour_serveur.status_code == 200:
            print("✅ SUCCÈS TOTAL : Vos 3 articles gratuits sont en ligne sur votre site Lignelife !")
        else:
            print(f"❌ Erreur lors de l'envoi : {mise_a_jour_serveur.text}")
            
    except Exception as e:
        print(f"❌ Une erreur réseau est survenue : {e}")

if __name__ == "__main__":
    machine_a_contenu_automatique()
