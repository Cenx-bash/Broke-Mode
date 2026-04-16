import json
import random
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

# ============================================================
# FAKE DATABASE FOR BROKE MODE MEAL FINDER
# A complete mock database system with meals, users, reviews,
# favorites, and usage analytics.
# ============================================================

class BrokeModeDatabase:
    """
    Fake database for the Broke Mode Meal Finder application.
    Provides realistic data and query methods for the website.
    """

    def __init__(self, data_dir: str = "broke_mode_data"):
        self.data_dir = data_dir
        self.meals: List[Dict] = []
        self.users: List[Dict] = []
        self.reviews: List[Dict] = []
        self.user_favorites: List[Dict] = []
        self.user_recent: List[Dict] = []
        self.usage_logs: List[Dict] = []

        # Create data directory if it doesn't exist
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Initialize with seed data
        self._seed_meals()
        self._seed_users()
        self._seed_reviews()
        self._seed_favorites()
        self._seed_recent_views()
        self._seed_usage_logs()

    # ============================================================
    # SEED DATA - MEALS (matches frontend exactly)
    # ============================================================
    def _seed_meals(self):
        """Initialize meal database with real-looking data around ADNU Naga"""
        self.meals = [
            {"id": 1, "name": "Sinangag + Itlog", "place": "Aling Nena's Carinderia", "category": "Carinderia",
             "price": 25, "distance": "80m", "distance_meters": 80, "rating": 4.3, "emoji": "🍳",
             "desc": "Classic garlic fried rice with egg. The real survival meal.",
             "lat": 13.6213, "lng": 123.1942, "tags": ["breakfast", "rice", "egg"], "is_vegetarian": False},
            {"id": 2, "name": "Pork BBQ (2pc)", "place": "Paseo Night Market", "category": "Street Food",
             "price": 30, "distance": "120m", "distance_meters": 120, "rating": 4.6, "emoji": "🍢",
             "desc": "Juicy charcoal-grilled pork sticks, best with rice.",
             "lat": 13.6208, "lng": 123.1935, "tags": ["grilled", "pork", "dinner"], "is_vegetarian": False},
            {"id": 3, "name": "Lugaw + Tokwa't Baboy", "place": "Mang Tino's", "category": "Carinderia",
             "price": 35, "distance": "200m", "distance_meters": 200, "rating": 4.1, "emoji": "🥣",
             "desc": "Hot lugaw with crispy tokwa and tender pork strips.",
             "lat": 13.6220, "lng": 123.1950, "tags": ["soup", "breakfast", "pork"], "is_vegetarian": False},
            {"id": 4, "name": "Fishball (10pc)", "place": "ADNU Gate 2 Stall", "category": "Street Food",
             "price": 20, "distance": "50m", "distance_meters": 50, "rating": 4.4, "emoji": "🐟",
             "desc": "Hot fishball with sweet-spicy sauce. Campus classic.",
             "lat": 13.6205, "lng": 123.1928, "tags": ["snack", "street", "sauce"], "is_vegetarian": False},
            {"id": 5, "name": "Pancit Bihon (Solo)", "place": "Ate Joy's Canteen", "category": "Campus Stall",
             "price": 40, "distance": "150m", "distance_meters": 150, "rating": 4.5, "emoji": "🍜",
             "desc": "Freshly cooked pancit with veggies and meat toppings.",
             "lat": 13.6218, "lng": 123.1945, "tags": ["noodles", "lunch", "veggies"], "is_vegetarian": False},
            {"id": 6, "name": "Adobo Rice Meal", "place": "ADNU Cafeteria", "category": "Campus Stall",
             "price": 55, "distance": "100m", "distance_meters": 100, "rating": 4.2, "emoji": "🍖",
             "desc": "Chicken adobo with garlic rice and a sunny-side egg.",
             "lat": 13.6215, "lng": 123.1940, "tags": ["adobo", "rice", "chicken"], "is_vegetarian": False},
            {"id": 7, "name": "Kwek-Kwek (5pc)", "place": "Paseo Night Market", "category": "Street Food",
             "price": 25, "distance": "120m", "distance_meters": 120, "rating": 4.7, "emoji": "🟠",
             "desc": "Orange battered quail eggs — Naga's best street snack.",
             "lat": 13.6209, "lng": 123.1937, "tags": ["snack", "egg", "street"], "is_vegetarian": False},
            {"id": 8, "name": "Tapsilog", "place": "RJ's Carenderia", "category": "Carinderia",
             "price": 70, "distance": "300m", "distance_meters": 300, "rating": 4.4, "emoji": "🥩",
             "desc": "Beef tapa, sinangag, and itlog. The holy trinity.",
             "lat": 13.6225, "lng": 123.1955, "tags": ["silog", "beef", "breakfast"], "is_vegetarian": False},
            {"id": 9, "name": "Siomai (4pc)", "place": "ADNU Gate 1 Stall", "category": "Campus Stall",
             "price": 30, "distance": "60m", "distance_meters": 60, "rating": 4.3, "emoji": "🥟",
             "desc": "Steamed pork siomai with soy-calamansi dipping sauce.",
             "lat": 13.6203, "lng": 123.1925, "tags": ["dimsum", "snack", "pork"], "is_vegetarian": False},
            {"id": 10, "name": "Burger Steak Meal", "place": "Jollibee Magsaysay", "category": "Fast Food",
             "price": 99, "distance": "500m", "distance_meters": 500, "rating": 4.6, "emoji": "🍔",
             "desc": "Two juicy beef patties in mushroom gravy. A treat.",
             "lat": 13.6230, "lng": 123.1960, "tags": ["burger", "fastfood", "gravy"], "is_vegetarian": False},
            {"id": 11, "name": "Palabok Solo", "place": "Chowking Naga", "category": "Fast Food",
             "price": 89, "distance": "450m", "distance_meters": 450, "rating": 4.3, "emoji": "🍝",
             "desc": "Thick rice noodles in seafood sauce with toppings.",
             "lat": 13.6228, "lng": 123.1958, "tags": ["noodles", "seafood", "fastfood"], "is_vegetarian": False},
            {"id": 12, "name": "Lumpiang Prito (3pc)", "place": "Manang's Corner", "category": "Street Food",
             "price": 15, "distance": "90m", "distance_meters": 90, "rating": 4.0, "emoji": "🌯",
             "desc": "Crispy fried spring rolls — vegetable-filled and hot.",
             "lat": 13.6210, "lng": 123.1932, "tags": ["snack", "veggie", "crispy"], "is_vegetarian": True},
            {"id": 13, "name": "Pork Sinigang (Tabo)", "place": "Aling Nena's Carinderia", "category": "Carinderia",
             "price": 60, "distance": "80m", "distance_meters": 80, "rating": 4.5, "emoji": "🥘",
             "desc": "Sour tamarind soup with pork and veggies, best with rice.",
             "lat": 13.6213, "lng": 123.1943, "tags": ["soup", "pork", "sour"], "is_vegetarian": False},
            {"id": 14, "name": "Halo-Halo (Merienda)", "place": "Jollibee Magsaysay", "category": "Fast Food",
             "price": 79, "distance": "500m", "distance_meters": 500, "rating": 4.8, "emoji": "🍧",
             "desc": "The Filipino dessert experience — ube, leche flan, crushed ice.",
             "lat": 13.6231, "lng": 123.1961, "tags": ["dessert", "cold", "sweet"], "is_vegetarian": True},
            {"id": 15, "name": "Banana Cue (3pc)", "place": "ADNU Gate 2 Stall", "category": "Street Food",
             "price": 15, "distance": "50m", "distance_meters": 50, "rating": 4.2, "emoji": "🍌",
             "desc": "Caramelized sugar-coated saba banana. Sweet afternoon fix.",
             "lat": 13.6206, "lng": 123.1929, "tags": ["dessert", "snack", "sweet"], "is_vegetarian": True},
            {"id": 16, "name": "Chicken Inasal Solo", "place": "Mang Inasal Naga", "category": "Fast Food",
             "price": 120, "distance": "600m", "distance_meters": 600, "rating": 4.7, "emoji": "🍗",
             "desc": "Unlimited rice with marinated Bacolod-style grilled chicken.",
             "lat": 13.6235, "lng": 123.1965, "tags": ["chicken", "grilled", "unlimited"], "is_vegetarian": False},
            {"id": 17, "name": "Goto (Beef Tripe Soup)", "place": "Mang Tino's", "category": "Carinderia",
             "price": 45, "distance": "200m", "distance_meters": 200, "rating": 4.0, "emoji": "🫕",
             "desc": "Warm, savory beef tripe congee — great for rainy days.",
             "lat": 13.6221, "lng": 123.1951, "tags": ["soup", "breakfast", "goto"], "is_vegetarian": False},
            {"id": 18, "name": "Campus Burger (No Fries)", "place": "ADNU Cafeteria", "category": "Campus Stall",
             "price": 45, "distance": "100m", "distance_meters": 100, "rating": 3.9, "emoji": "🍔",
             "desc": "Student favorite — simple beef patty with special sauce.",
             "lat": 13.6216, "lng": 123.1941, "tags": ["burger", "snack", "campus"], "is_vegetarian": False},
        ]

    def _seed_users(self):
        """Generate fake users for the system"""
        self.users = [
            {"id": 1, "username": "broke_student", "email": "student@adnu.edu.ph", "budget_preference": 50,
             "dietary_pref": None, "join_date": "2024-01-15", "total_saved": 0, "avatar": "🎓"},
            {"id": 2, "username": "night_craver", "email": "craver@example.com", "budget_preference": 80,
             "dietary_pref": None, "join_date": "2024-02-20", "total_saved": 0, "avatar": "🌙"},
            {"id": 3, "username": "vegan_warrior", "email": "vegan@adnu.edu.ph", "budget_preference": 60,
             "dietary_pref": "vegetarian", "join_date": "2024-01-30", "total_saved": 0, "avatar": "🥬"},
            {"id": 4, "username": "foodie_francis", "email": "francis@example.com", "budget_preference": 120,
             "dietary_pref": None, "join_date": "2024-02-01", "total_saved": 0, "avatar": "🍽️"},
        ]

    def _seed_reviews(self):
        """Generate fake reviews for meals"""
        review_templates = [
            "Solid meal for the price! 👌",
            "Could be better but sulit naman.",
            "My go-to pag walang pera 💯",
            "Medyo maalat pero okay na.",
            "Super sarap! Will order again!",
            "Mabilis service, mainit pa pagkain.",
            "Not bad, pwede na.",
            "The best value near campus!",
            "Maliit serving pero masarap.",
            "Budget-friendly and filling!",
        ]
        self.reviews = []
        review_id = 1
        for meal in self.meals:
            num_reviews = random.randint(2, 6)
            for _ in range(num_reviews):
                self.reviews.append({
                    "id": review_id,
                    "meal_id": meal["id"],
                    "user_id": random.choice(self.users)["id"],
                    "rating": round(random.uniform(3.0, 5.0), 1),
                    "comment": random.choice(review_templates),
                    "date": f"2024-{random.randint(1,3):02d}-{random.randint(1,28):02d}",
                    "likes": random.randint(0, 15)
                })
                review_id += 1

    def _seed_favorites(self):
        """Seed some initial favorite relationships"""
        self.user_favorites = [
            {"user_id": 1, "meal_id": 4, "added_at": "2024-02-10T08:30:00"},
            {"user_id": 1, "meal_id": 7, "added_at": "2024-02-11T12:15:00"},
            {"user_id": 1, "meal_id": 12, "added_at": "2024-02-12T18:45:00"},
            {"user_id": 2, "meal_id": 2, "added_at": "2024-02-09T20:00:00"},
            {"user_id": 2, "meal_id": 10, "added_at": "2024-02-10T14:30:00"},
            {"user_id": 3, "meal_id": 12, "added_at": "2024-02-08T11:00:00"},
            {"user_id": 3, "meal_id": 14, "added_at": "2024-02-11T16:20:00"},
        ]

    def _seed_recent_views(self):
        """Seed recent view history for users"""
        self.user_recent = [
            {"user_id": 1, "meal_id": 4, "viewed_at": "2024-02-14T12:00:00"},
            {"user_id": 1, "meal_id": 1, "viewed_at": "2024-02-14T11:45:00"},
            {"user_id": 1, "meal_id": 7, "viewed_at": "2024-02-13T19:30:00"},
            {"user_id": 2, "meal_id": 16, "viewed_at": "2024-02-14T10:15:00"},
            {"user_id": 2, "meal_id": 10, "viewed_at": "2024-02-14T09:00:00"},
            {"user_id": 3, "meal_id": 14, "viewed_at": "2024-02-13T15:30:00"},
            {"user_id": 3, "meal_id": 12, "viewed_at": "2024-02-13T12:00:00"},
            {"user_id": 3, "meal_id": 4, "viewed_at": "2024-02-12T18:00:00"},
        ]

    def _seed_usage_logs(self):
        """Seed usage analytics logs"""
        actions = ["search", "view_meal", "filter_category", "sort", "add_favorite", "remove_favorite", "map_interaction"]
        for i in range(50):
            self.usage_logs.append({
                "id": i + 1,
                "user_id": random.choice([1, 2, 3, 4, None]),
                "action": random.choice(actions),
                "details": {},
                "timestamp": f"2024-02-{random.randint(1,14):02d}T{random.randint(8,22):02d}:{random.randint(0,59):02d}:00",
                "session_id": f"sess_{random.randint(1000, 9999)}"
            })

    # ============================================================
    # PUBLIC QUERY METHODS
    # ============================================================

    def get_all_meals(self) -> List[Dict]:
        """Return all meals in the database"""
        return self.meals.copy()

    def get_meal_by_id(self, meal_id: int) -> Optional[Dict]:
        """Get a single meal by its ID"""
        for meal in self.meals:
            if meal["id"] == meal_id:
                return meal.copy()
        return None

    def get_meals_by_budget(self, max_price: int) -> List[Dict]:
        """Filter meals by maximum price"""
        return [m for m in self.meals if m["price"] <= max_price]

    def get_meals_by_category(self, category: str) -> List[Dict]:
        """Filter meals by category (Carinderia, Street Food, etc.)"""
        return [m for m in self.meals if m["category"].lower() == category.lower()]

    def get_meals_by_tag(self, tag: str) -> List[Dict]:
        """Filter meals by tag (breakfast, snack, etc.)"""
        return [m for m in self.meals if tag.lower() in [t.lower() for t in m["tags"]]]

    def get_vegetarian_meals(self) -> List[Dict]:
        """Get all vegetarian-friendly meals"""
        return [m for m in self.meals if m["is_vegetarian"]]

    def search_meals(self, query: str) -> List[Dict]:
        """Search meals by name, place, or category"""
        query_lower = query.lower()
        results = []
        for meal in self.meals:
            if (query_lower in meal["name"].lower() or
                query_lower in meal["place"].lower() or
                query_lower in meal["category"].lower()):
                results.append(meal)
        return results

    def get_cheapest_meal(self) -> Optional[Dict]:
        """Get the cheapest meal available"""
        if not self.meals:
            return None
        return min(self.meals, key=lambda m: m["price"])

    def get_most_expensive_meal(self) -> Optional[Dict]:
        """Get the most expensive meal"""
        if not self.meals:
            return None
        return max(self.meals, key=lambda m: m["price"])

    def get_best_value_meals(self, limit: int = 5) -> List[Dict]:
        """Get meals with best price-to-rating ratio"""
        sorted_meals = sorted(self.meals, key=lambda m: m["rating"] / m["price"], reverse=True)
        return sorted_meals[:limit]

    def get_top_rated_meals(self, limit: int = 5) -> List[Dict]:
        """Get highest rated meals"""
        sorted_meals = sorted(self.meals, key=lambda m: m["rating"], reverse=True)
        return sorted_meals[:limit]

    def get_nearby_meals(self, lat: float, lng: float, radius_meters: int = 500) -> List[Dict]:
        """Get meals within a certain radius (simplified distance calculation)"""
        from math import radians, sin, cos, sqrt, atan2

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371000  # Earth radius in meters
            phi1, phi2 = radians(lat1), radians(lat2)
            dphi = radians(lat2 - lat1)
            dlambda = radians(lon2 - lon1)

            a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            return R * c

        nearby = []
        for meal in self.meals:
            distance = haversine(lat, lng, meal["lat"], meal["lng"])
            if distance <= radius_meters:
                meal_copy = meal.copy()
                meal_copy["distance_meters_calc"] = int(distance)
                nearby.append(meal_copy)

        return sorted(nearby, key=lambda m: m["distance_meters_calc"])

    # ============================================================
    # FAVORITES METHODS
    # ============================================================

    def get_user_favorites(self, user_id: int) -> List[Dict]:
        """Get favorite meals for a specific user"""
        fav_meal_ids = [f["meal_id"] for f in self.user_favorites if f["user_id"] == user_id]
        return [m for m in self.meals if m["id"] in fav_meal_ids]

    def add_favorite(self, user_id: int, meal_id: int) -> bool:
        """Add a meal to user's favorites"""
        if any(f["user_id"] == user_id and f["meal_id"] == meal_id for f in self.user_favorites):
            return False
        self.user_favorites.append({
            "user_id": user_id,
            "meal_id": meal_id,
            "added_at": datetime.now().isoformat()
        })
        return True

    def remove_favorite(self, user_id: int, meal_id: int) -> bool:
        """Remove a meal from user's favorites"""
        initial_len = len(self.user_favorites)
        self.user_favorites = [f for f in self.user_favorites if not (f["user_id"] == user_id and f["meal_id"] == meal_id)]
        return len(self.user_favorites) < initial_len

    # ============================================================
    # RECENT VIEWS METHODS
    # ============================================================

    def add_recent_view(self, user_id: int, meal_id: int) -> None:
        """Log a meal view for a user"""
        self.user_recent.append({
            "user_id": user_id,
            "meal_id": meal_id,
            "viewed_at": datetime.now().isoformat()
        })
        # Keep only last 20 views per user
        user_views = [v for v in self.user_recent if v["user_id"] == user_id]
        if len(user_views) > 20:
            to_remove = user_views[:-20]
            self.user_recent = [v for v in self.user_recent if v not in to_remove]

    def get_recent_views(self, user_id: int, limit: int = 8) -> List[Dict]:
        """Get recently viewed meals for a user"""
        user_views = sorted(
            [v for v in self.user_recent if v["user_id"] == user_id],
            key=lambda v: v["viewed_at"],
            reverse=True
        )[:limit]
        recent_meals = []
        for view in user_views:
            meal = self.get_meal_by_id(view["meal_id"])
            if meal:
                meal["viewed_at"] = view["viewed_at"]
                recent_meals.append(meal)
        return recent_meals

    # ============================================================
    # STATISTICS & ANALYTICS
    # ============================================================

    def get_price_stats(self) -> Dict:
        """Get price statistics for all meals"""
        prices = [m["price"] for m in self.meals]
        return {
            "min": min(prices),
            "max": max(prices),
            "avg": round(sum(prices) / len(prices), 2),
            "median": sorted(prices)[len(prices)//2]
        }

    def get_category_counts(self) -> Dict:
        """Get count of meals per category"""
        counts = {}
        for meal in self.meals:
            counts[meal["category"]] = counts.get(meal["category"], 0) + 1
        return counts

    def get_most_popular_meals(self, limit: int = 5) -> List[Dict]:
        """Get most favorited meals"""
        fav_counts = {}
        for fav in self.user_favorites:
            fav_counts[fav["meal_id"]] = fav_counts.get(fav["meal_id"], 0) + 1

        meals_with_counts = []
        for meal in self.meals:
            meal_copy = meal.copy()
            meal_copy["favorite_count"] = fav_counts.get(meal["id"], 0)
            meals_with_counts.append(meal_copy)

        return sorted(meals_with_counts, key=lambda m: m["favorite_count"], reverse=True)[:limit]

    def get_user_summary(self, user_id: int) -> Dict:
        """Get a summary of user activity"""
        favorites = len([f for f in self.user_favorites if f["user_id"] == user_id])
        recent_views = len([v for v in self.user_recent if v["user_id"] == user_id])
        user = next((u for u in self.users if u["id"] == user_id), None)

        return {
            "user_id": user_id,
            "username": user["username"] if user else "Unknown",
            "favorite_count": favorites,
            "recent_views_count": recent_views,
            "budget_preference": user["budget_preference"] if user else None,
        }

    # ============================================================
    # REVIEW METHODS
    # ============================================================

    def get_reviews_for_meal(self, meal_id: int) -> List[Dict]:
        """Get all reviews for a specific meal"""
        return [r for r in self.reviews if r["meal_id"] == meal_id]

    def add_review(self, meal_id: int, user_id: int, rating: float, comment: str) -> Dict:
        """Add a new review for a meal"""
        new_id = max([r["id"] for r in self.reviews]) + 1 if self.reviews else 1
        review = {
            "id": new_id,
            "meal_id": meal_id,
            "user_id": user_id,
            "rating": rating,
            "comment": comment,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "likes": 0
        }
        self.reviews.append(review)

        # Update meal's average rating
        meal_reviews = self.get_reviews_for_meal(meal_id)
        avg_rating = sum(r["rating"] for r in meal_reviews) / len(meal_reviews)
        for meal in self.meals:
            if meal["id"] == meal_id:
                meal["rating"] = round(avg_rating, 1)
                break

        return review

    # ============================================================
    # RECOMMENDATION ENGINE
    # ============================================================

    def get_recommendations(self, user_id: int, limit: int = 5) -> List[Dict]:
        """
        Get personalized meal recommendations based on user's
        favorites, recent views, and budget preference.
        """
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            return self.get_top_rated_meals(limit)

        # Get user's favorite categories and tags
        fav_meals = self.get_user_favorites(user_id)
        recent_meals = self.get_recent_views(user_id, limit=10)

        # Build preference profile
        category_weights = {}
        tag_weights = {}
        price_pref = user.get("budget_preference", 60)

        for meal in fav_meals + recent_meals:
            category_weights[meal["category"]] = category_weights.get(meal["category"], 0) + 1
            for tag in meal["tags"]:
                tag_weights[tag] = tag_weights.get(tag, 0) + 1

        # Score all meals
        viewed_ids = {m["id"] for m in recent_meals}
        fav_ids = {m["id"] for m in fav_meals}

        scored_meals = []
        for meal in self.meals:
            if meal["id"] in viewed_ids or meal["id"] in fav_ids:
                continue

            score = 0
            # Category match
            score += category_weights.get(meal["category"], 0) * 2
            # Tag match
            for tag in meal["tags"]:
                score += tag_weights.get(tag, 0)
            # Price fit (closer to preference = higher score)
            price_diff = abs(meal["price"] - price_pref)
            score += max(0, 10 - price_diff) * 0.5
            # Rating bonus
            score += meal["rating"] * 2

            scored_meals.append((meal, score))

        scored_meals.sort(key=lambda x: x[1], reverse=True)
        return [meal for meal, _ in scored_meals[:limit]]

    # ============================================================
    # DATA EXPORT & PERSISTENCE
    # ============================================================

    def export_to_json(self, filename: str = None) -> str:
        """Export entire database to JSON file"""
        if filename is None:
            filename = os.path.join(self.data_dir, f"broke_mode_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

        export_data = {
            "meals": self.meals,
            "users": self.users,
            "reviews": self.reviews,
            "user_favorites": self.user_favorites,
            "user_recent": self.user_recent,
            "usage_logs": self.usage_logs,
            "export_timestamp": datetime.now().isoformat()
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

        return filename

    def save_state(self) -> None:
        """Save current database state to disk"""
        self.export_to_json(os.path.join(self.data_dir, "latest_backup.json"))

    def get_summary(self) -> Dict:
        """Get a quick summary of database contents"""
        return {
            "total_meals": len(self.meals),
            "total_users": len(self.users),
            "total_reviews": len(self.reviews),
            "total_favorites": len(self.user_favorites),
            "total_recent_views": len(self.user_recent),
            "total_usage_logs": len(self.usage_logs),
            "categories": self.get_category_counts(),
            "price_range": {"min": 15, "max": 120},
            "avg_rating": round(sum(m["rating"] for m in self.meals) / len(self.meals), 2)
        }


# ============================================================
# USAGE EXAMPLES & TESTING
# ============================================================

def demo_database():
    """Demonstrate database functionality"""
    print("🍚 BROKE MODE DATABASE DEMO")
    print("=" * 50)

    # Initialize database
    db = BrokeModeDatabase()
    print(f"✅ Database initialized")

    # Show summary
    summary = db.get_summary()
    print(f"\n📊 DATABASE SUMMARY:")
    for key, value in summary.items():
        print(f"   {key}: {value}")

    # Query examples
    print("\n🔍 QUERY EXAMPLES:")

    # Get cheap meals
    cheap = db.get_meals_by_budget(30)
    print(f"\n   Meals under ₱30: {len(cheap)}")
    for meal in cheap[:3]:
        print(f"      - {meal['name']} (₱{meal['price']})")

    # Get best value
    best = db.get_best_value_meals(3)
    print(f"\n   Best Value Meals:")
    for meal in best:
        print(f"      - {meal['name']} (₱{meal['price']} | ⭐{meal['rating']})")

    # Vegetarian options
    veg = db.get_vegetarian_meals()
    print(f"\n   Vegetarian Options: {len(veg)}")
    for meal in veg:
        print(f"      - {meal['name']}")

    # User favorites
    print(f"\n   User 1 Favorites:")
    favs = db.get_user_favorites(1)
    for meal in favs:
        print(f"      - {meal['name']}")

    # Recommendations
    print(f"\n   Personalized Recommendations for User 1:")
    recs = db.get_recommendations(1, 3)
    for meal in recs:
        print(f"      - {meal['name']} (score based on preferences)")

    # Nearby meals
    print(f"\n   Nearby meals (100m radius from ADNU):")
    nearby = db.get_nearby_meals(13.6215, 123.194, 100)
    for meal in nearby:
        print(f"      - {meal['name']} ({meal['distance_meters_calc']}m away)")

    # Export
    export_file = db.export_to_json()
    print(f"\n💾 Database exported to: {export_file}")

    print("\n" + "=" * 50)
    print("✅ Demo complete!")


if __name__ == "__main__":
    demo_database()
