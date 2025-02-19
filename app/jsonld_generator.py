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
            },
            "image": data.get("image", "https://example.com/image.jpg"),  
            "publisher": {
                "@type": "Organization",
                "name": data.get("publisher", "Nom de l'éditeur"),
                "logo": {
                    "@type": "ImageObject",
                    "url": data.get("publisherLogo", "https://example.com/logo.jpg")
                }
            }
        }
    elif content_type == "Product":
        return {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": data.get("name", "Produit inconnu"),
            "brand": data.get("brand", "Marque inconnu"),
            "price": data.get("price", "0.00"),
            "description": data.get("description", "Description non fourni"),
            "sku": data.get("sku", "SKU inconnu"),  
            "mpn": data.get("mpn", "MPN inconnu"),  
            "image": data.get("image", "https://example.com/image.jpg"),  
            "offers": {
                "@type": "Offer",
                "priceCurrency": data.get("priceCurrency", "USD"),
                "price": data.get("price", "0.00"),
                "availability": data.get("availability", "https://schema.org/InStock"),
                "url": data.get("offerUrl", "https://example.com/produit")
            }
        }
    elif content_type == "Organization":
        return {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": data.get("name", "Nom de l'organisation inconnu"),
            "url": data.get("url", "https://example.com"),
            "logo": data.get("logo", "https://example.com/logo.png"),
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": data.get("telephone", "000-000-0000"),
                "contactType": data.get("contactType", "Service client"),
                "email": data.get("email", "contact@example.com"),  
                "areaServed": data.get("areaServed", "Zone desservie")  
            },
            "address": {
                "@type": "PostalAddress",
                "streetAddress": data.get("streetAddress", "Adresse inconnue"),
                "addressLocality": data.get("addressLocality", "Localité inconnue"),
                "addressRegion": data.get("addressRegion", "Région inconnue"),
                "postalCode": data.get("postalCode", "Code postal inconnu"),
                "addressCountry": data.get("addressCountry", "Pays inconnu")
            }
        }
    elif content_type == "Event":
        return {
            "@context": "https://schema.org",
            "@type": "Event",
            "name": data.get("name", "Nom de l'événement inconnu"),
            "startDate": data.get("startDate", "2025-02-17T00:00:00Z"),
            "endDate": data.get("endDate", "2025-02-18T00:00:00Z"),
            "location": {
                "@type": "Place",
                "name": data.get("locationName", "Lieu inconnu"),
                "address": data.get("address", "Adresse inconnu")
            },
            "description": data.get("description", "Description non fournie"),  
            "image": data.get("image", "https://example.com/image.jpg"),  
            "performer": {
                "@type": "Person",
                "name": data.get("performer", "Nom du performer") 
            }
        }
    else:
        return {
            "error": "Type de contenu non supporté"
        }