// Group-1
//  1.. Searching and Sorting: 
// 1. Add and store student details (ID, Name, CGPA) using dynamically allocated memory.
//  2. Expand the student list using realloc() as new entries are added.
//  3. Implement Linear Search and Binary Search to find student records by ID
#include <iostream>
#include <cstdlib>   // for malloc, realloc, free
#include <algorithm> // for sort
using namespace std;

struct Student
{
    int id;
    char name[50];
    float cgpa;
};

int linearSearch(Student *s, int n, int id)
{
    for (int i = 0; i < n; i++)
    {
        if (s[i].id == id)
            return i;
    }
    return -1;
}

int binarySearch(Student *s, int n, int id)
{
    int l = 0, r = n - 1;
    while (l <= r)
    {
        int mid = (l + r) / 2;
        if (s[mid].id == id)
            return mid;
        else if (s[mid].id < id)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return -1;
}

int main()
{
    int n = 0, ch, id;
    Student *s = (Student *)malloc(sizeof(Student)); // first block

    while (true)
    {
        cout << "\n1.Add  2.Display  3.Linear Search  4.Binary Search  5.Exit\nEnter choice: ";
        cin >> ch;

        if (ch == 1)
        {
            s = (Student *)realloc(s, (n + 1) * sizeof(Student)); // expand list
            cout << "Enter ID Name CGPA: ";
            cin >> s[n].id >> s[n].name >> s[n].cgpa;
            n++;
        }
        else if (ch == 2)
        {
            cout << "\nID\tName\tCGPA\n";
            for (int i = 0; i < n; i++)
                cout << s[i].id << "\t" << s[i].name << "\t" << s[i].cgpa << endl;
        }
        else if (ch == 3)
        {
            cout << "Enter ID to search: ";
            cin >> id;
            int pos = linearSearch(s, n, id);
            if (pos == -1)
                cout << "Record not found!\n";
            else
                cout << "Found: " << s[pos].name << " " << s[pos].cgpa << endl;
        }
        else if (ch == 4)
        {
            sort(s, s + n, [](Student a, Student b)
                 { return a.id < b.id; });
            cout << "Enter ID to search: ";
            cin >> id;
            int pos = binarySearch(s, n, id);
            if (pos == -1)
                cout << "Record not found!\n";
            else
                cout << "Found: " << s[pos].name << " " << s[pos].cgpa << endl;
        }
        else
            break;
    }
    free(s);
    return 0;
}
