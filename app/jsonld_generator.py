def generate_jsonld(content_type, data):
    if content_type == "Article":
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": data.get("headline", "Titre par défaut"),
            "author": {
                "@type": "Person",
                "name": data.get("author", "Auteur inconnu")
            },
            "datePublished": data.get("datePublished", "2025-02-17"),
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": data.get("url", "https://example.com")
            }
        }
    elif content_type == "Product":
        return {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": data.get("name", "Produit inconnu"),
            "brand": data.get("brand", "Marque inconnue"),
            "description": data.get("description", "Description non fournie"),
            "sku": data.get("sku", "00000")
        }
    else:
        return {"error": "Type de contenu non supporté"}
