from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"email": "alice@example.com", "password": "Password123!"},
    {"email": "bob@example.com", "password": "Password123!"},
    {"email": "mathav@example.com", "password": "Password123!"}
]

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    email = data.get('email')
    current_password = data.get('currentPassword')
    new_password = data.get('newPassword')

    # Find user by email
    user = next((u for u in users if u['email'] == email), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Verify current password
    if user['password'] != current_password:
        return jsonify({"error": "Current password is incorrect"}), 400

    # Validate new password
    if (not new_password or len(new_password) < 8 or
        not any(c.isupper() for c in new_password) or
        not any(c.islower() for c in new_password) or
        not any(c.isdigit() for c in new_password) or
        not any(c in "!@#$%^&*" for c in new_password)):
        return jsonify({"error": "Invalid new password. Password must be at least 8 characters long and include uppercase, lowercase, digit, and special character."}), 400

    # Update password
    user['password'] = new_password
    return jsonify({"message": "Password changed successfully"}), 200

if __name__ == '__main__':
    app.run(port=3000)
