// Secure Login System (C++) - Practice Demo
// NOTE: Uses salt + std::hash for simplicity. std::hash is NOT cryptographically secure.
// Do not use this pattern in production. This is for learning/demo only.

#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <sstream>
#include <functional> // std::hash
#include <random>

using namespace std;

static const string USERS_DB = "users.txt";

string generateSalt(size_t length = 16) {
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, sizeof(alphanum) - 2);

    string s;
    s.reserve(length);
    for (size_t i = 0; i < length; ++i) {
        s.push_back(alphanum[dis(gen)]);
    }
    return s;
}

// "Demo hash": salted std::hash — not cryptographically secure
string demoHash(const string& password, const string& salt) {
    string salted = salt + ":" + password;
    size_t h = hash<string>{}(salted);
    // Convert to hex
    stringstream ss;
    ss << std::hex << h;
    return ss.str();
}

void registerUser() {
    string user, pass;
    cout << "Enter username: ";
    cin >> user;
    cout << "Enter password: ";
    cin >> pass;

    // Check if user exists
    ifstream in(USERS_DB);
    string line;
    while (getline(in, line)) {
        if (line.rfind(user + ":", 0) == 0) {
            cout << "User already exists.\n";
            return;
        }
    }
    in.close();

    string salt = generateSalt();
    string digest = demoHash(pass, salt);

    ofstream out(USERS_DB, ios::app);
    out << user << ":" << salt << ":" << digest << "\n";
    out.close();

    cout << "User registered successfully!\n";
}

void loginUser() {
    string user, pass;
    cout << "Enter username: ";
    cin >> user;
    cout << "Enter password: ";
    cin >> pass;

    ifstream in(USERS_DB);
    if (!in) {
        cout << "No users database found. Please register first.\n";
        return;
    }

    string line;
    while (getline(in, line)) {
        // Format: username:salt:digest
        size_t p1 = line.find(':');
        size_t p2 = line.find(':', p1 + 1);
        if (p1 == string::npos || p2 == string::npos) continue;
        string u = line.substr(0, p1);
        string salt = line.substr(p1 + 1, p2 - p1 - 1);
        string digest = line.substr(p2 + 1);

        if (u == user) {
            string attempt = demoHash(pass, salt);
            if (attempt == digest) {
                cout << "Login successful!\n";
            } else {
                cout << "Invalid password.\n";
            }
            return;
        }
    }
    cout << "User not found.\n";
}

int main() {
    cout << "Secure Login System (Educational)\n";
    cout << "1) Register\n2) Login\nSelect: ";
    int choice = 0;
    if (!(cin >> choice)) return 0;

    if (choice == 1) registerUser();
    else if (choice == 2) loginUser();
    else cout << "Invalid choice.\n";
    return 0;
}
