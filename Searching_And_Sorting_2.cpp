//  2.Searching and Sorting: 
// 1. Add and store student details (ID, Name, CGPA) using dynamically allocated memory.
//  2. Expand the student list using realloc() as new entries are added.
//  3. Implement at least two Sorting Algorithms (Bubble Sort, Selection Sort, or Insertion Sort) to sort 
// student records by:
//   Name (Alphabetically)
//   CGPA (Ascending/Descending)
 
#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

struct Student
{
    int id;
    char name[50];
    float cgpa;
};

void bubbleSortName(Student *s, int n)
{
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (strcmp(s[j].name, s[j + 1].name) > 0)
                swap(s[j], s[j + 1]);
}

void selectionSortCGPA(Student *s, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int max = i;
        for (int j = i + 1; j < n; j++)
            if (s[j].cgpa > s[max].cgpa)
                max = j;
        swap(s[i], s[max]);
    }
}

int main()
{
    int n = 0, ch;
    Student *s = (Student *)malloc(sizeof(Student));
    while (true)
    {
        cout << "\n1.Add 2.Display 3.Sort by Name 4.Sort by CGPA 5.Exit\nEnter choice: ";
        cin >> ch;
        if (ch == 1)
        {
            s = (Student *)realloc(s, (n + 1) * sizeof(Student));
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
            bubbleSortName(s, n);
            cout << "Sorted by Name!\n";
        }
        else if (ch == 4)
        {
            selectionSortCGPA(s, n);
            cout << "Sorted by CGPA!\n";
        }
        else
            break;
    }
    free(s);
    return 0;
}
