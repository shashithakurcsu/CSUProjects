class CSUSMRecommendationSystem:
    def __init__(self):
        # Instantiate an empty dictionary
        self.user_data = {}

    def insert_user(self, user_id, posts):
        self.user_data[user_id] = posts
        print(f"Inserted posts for user {user_id}")

    def retrieve_user_posts(self, user_id):
        return self.user_data.get(user_id, None)

    def delete_user(self, user_id):
        if user_id in self.user_data:
            del self.user_data[user_id]
            print(f"Deleted data for user {user_id}")
        else:
            print(f"User {user_id} not found")

# Example usage
if __name__ == "__main__":
    recommendation_system = CSUSMRecommendationSystem()

    # Inserting user data
    recommendation_system.insert_user("user1", ["post1", "post2", "post3"])
    recommendation_system.insert_user("user2", ["post4", "post5", "post6"])
    recommendation_system.insert_user("user3", ["post7", "post8", "post9"])

    # Retrieving user posts
    print("User1's posts:", recommendation_system.retrieve_user_posts("user1"))
    print("User2's posts:", recommendation_system.retrieve_user_posts("user2"))
    print("User3's posts:", recommendation_system.retrieve_user_posts("user3"))

    # Deleting a user
    recommendation_system.delete_user("user1")
    print("User1's posts after deletion:", recommendation_system.retrieve_user_posts("user1"))

    # Retrieving user posts for a non-existing user
    print("User4's posts:", recommendation_system.retrieve_user_posts("user4"))
