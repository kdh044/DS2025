#pragma once
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Music {
private:
    string title;
    string artist;
    string album;
    int year;

public:
    // 생성자
    Music(string t, string a, string al, int y)
        : title(t), artist(a), album(al), year(y) {}

    // 기본 생성자 (검색 실패 시 사용)
    Music() : title(""), artist(""), album(""), year(0) {}

    // Getter 함수들
    string getTitle() const { return title; }
    string getArtist() const { return artist; }
    string getAlbum() const { return album; }
    int getYear() const { return year; }
};

class MusicStreamingService {
private:
    string service_name;
    vector<Music> music_list;

public:
    // 생성자
    MusicStreamingService(string service_name) {
        this->service_name = service_name;
    }

    // 음악 추가 기능
    void addMusic(string title, string artist, string album, int year) {
        Music new_music(title, artist, album, year);
        music_list.push_back(new_music);
        cout << title << " by " << artist << " added to " << service_name << endl;
    }

    // 전체 음악 목록 출력
    void showAllMusic() const {
        cout << "\n===== Music List in " << service_name << " =====" << endl;
        for (const auto& m : music_list) {
            cout << m.getTitle() << " by " << m.getArtist()
                 << " added to " << service_name << endl;
        }
    }
    
    
    //음악 찾아주는 서비스(title)
    Music* searchByTitle(string title){ //*들어가면 주소값을 반환하는구나 기억해두기
        for (int i = 0; i < music_list.size(); i++){
            if (music_list[i].getTitle() == title){
                return & music_list[i];
            }
        }   return NULL; //없어서 null
    }

     //음악 찾아주는 서비스(Artist)
     vector<Music*> searchByArtist(string artist){
        vector<Music*> result;
        for(int i = 0; i < music_list.size(); i++){
            if(music_list[i].getArtist() == artist){
                result.push_back(&music_list[i]);  //music list의 i번째 칸에 대한 주소값
         }
        }   return result;
    }  

};

// 디버깅 F5,F9,F11
