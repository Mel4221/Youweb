// JavaScript source code

/**
 * From here down it starts all the code from the media player
 * 
 * 
 ***/

// Get elements
const searchInput = document.getElementById('SearchInput');
const playBtn = document.getElementById('PlayBtn');
const pauseBtn = document.getElementById('PauseBtn');
//const stopBtn = document.getElementById('StopBtn');
const muteBtn = document.getElementById('MuteBtn');
const progressBar = document.getElementById('ProgressBar');
const progressBarNumber = document.getElementById('ProgressBarNumber');
const volumeControl = document.getElementById('VolumeControl');
const audioPlayer = document.getElementById('audioPlayer');
const playingSong = document.getElementById('PlayingSong');
const playBack = document.getElementById('PlayBack');
const playFoward = document.getElementById('PlayFoward');
const repeatMode = document.getElementById('RepeatAll');
const aleatoryMode = document.getElementById('Aleatory');
const songsList = document.querySelectorAll('#SongsList .Song');
//const svg_icon0 = document.getElementById('svg_icon0');
//const svg_icon1 = document.getElementById('svg_icon1');

//display: none

// muteBtn.innerHTML = "&#128266;";
/*
repeatMode.classList.remove("switchable");
repeatMode.classList.add("default");
*/
/**PlayBack#RepeatAll#Aleatory#PlayFoward**/

var stop_playallfoward = false;
var play_index = 0;
var song_paused = true;
var song_repeat = false;
var play_aleatory = false;
var id = null;
// Check if the file exist or not
/*
 async function fileExists(url) {
try {
   const response = await fetch(url, {
       method: 'HEAD' // Only fetch headers
   });
   if (response.ok) {
       // File exists
       return true;
   } else {
       // File does not exist
       return false;
   }
} catch (error) {
   // Error occurred, possibly network issue
   console.error('Error checking file existence:', error);
   return false;
}
}
*/
/*
       async function PlayAllFoward_SetClickEvent(song)
       {
          
           return new Promise((resolve)=>
           {
               song.addEventListener('click', async () => {
                   const audioPlayer = document.getElementById('audioPlayer');
                   audioPlayer.src = song.getAttribute('data-src');
                   //debugging area
                   console.log("Goal: "+goal+" Current: "+current);
                   //console.log(song);
                   console.log(song.getAttribute('data-src'));
                   //debugging area
                   audioPlayer.play();
                           // Resolve the promise when the song ends
                   audioPlayer.onended = () => {
                       resolve(); // Song has ended
                   };
                   current++;
                   if(current>=goal-1 && repeatMode.value == "all")
                   {
                       console.log("Again...");
                       PlayAllFoward();
                       return;
                   }
                   if(stop_playallfoward)
                   {
                       console.log("Stop playing all foward requested");
                       return;
                   }
               });
 
           });
           
       }
       */
const AudioPlay = () => {
    try {
        audioPlayer.play();
    } catch {
        console.log("Failed to play the given song!!!");
    }
};
const Play = (index) => {


    try {
        console.log("Play request..: " + songsList[play_index].textContent);
        console.log("Index..: " + index);
        songsList[index].click();
    } catch {
        console.log("Failed to  play the index..: " + index);
    }

};

const SwapSvg = () => {
    if (song_paused) {
        song_paused = false;
        playBtn.style.display = "none";
        pauseBtn.style.display = "flex";
        console.log("Is song paused..: " + song_paused);
        return;
    } else {
        song_paused = true;
        playBtn.style.display = "flex";
        pauseBtn.style.display = "none";
        console.log("Is song paused..: " + song_paused);

    }
};
const RepeatOrContinue = () => {
    console.log("RepeatOrContinue..: " + song_repeat == false ? "continue..." : "repeat...");
    if (play_aleatory) {
        Play(ShuffleIndex());
        return;
    }
    if (song_repeat == false) {
        play_index++;
        if (play_index > songsList.length - 1) {
            play_index = 0;
        }
        console.log("Moving foward play_index increased..: " + play_index);
        PlayAllFoward();
        return;
    } else {

        console.log("Repeatting play_index...: " + play_index);
        console.log("Song..: " + songsList[play_index].textContent);
        Play(play_index);
        return;
    }

};
audioPlayer.onended = RepeatOrContinue;

async function PlayAllFoward_Click(song) {

    console.log("Clicking...: " + song.textContent);
    song.click();
    return new Promise((resolve) => {

        audioPlayer.onended = () => {
            resolve(); // Song has ended
            audioPlayer.onended = RepeatOrContinue;
        };
    });

}

// Function to handle song selection and playing
async function PlayAllFoward() {
    console.log("Playing Foward started at play_index..: " + play_index);
    let current;
    const goal = songsList.length;
    console.log("List Items: " + songsList.length);

    for (let s = play_index; s < songsList.length; s++)//for (const song of songsList) 
    {
        // Wait for the song to finish playing

        await PlayAllFoward_Click(songsList[s]);
        current++;
        if (song_repeat) {
            RepeatOrContinue();
            return;
        }
        if (current == goal - 1 &&
            song_repeat == false) {
            play_index = 0;
            PlayAllFoward();
            return;
        }
    }

}
function ShuffleIndex() {
    //let index = Math.round(Math.random(0,songsList.length-1)*100);
    let index = Math.floor(Math.random() * songsList.length);

    play_index = index;
    console.log("Random index given..: " + play_index);
    return index;
}


function PlaySong() {
    var song = audioPlayer.getAttribute('data-src');
    SwapSvg();
    if (song != null) {
        console.log('File exists: ' + song);
        //audioPlayer.play();
        //AudioPlay();
        PlayAllFoward();
        return;
    } else {
        console.log('File does not exist.');
        console.log("Playing Song Failed!!!");
        console.log("Playing the whole list instead...");
        PlayAllFoward();

    }


}

// Function to filter songs
function SearchSong() {
    const searchValue = searchInput.value.toLowerCase();

    songsList.forEach(function (item) {
        const text = item.textContent.toLowerCase();

        if (text.includes(searchValue)) {
            item.style.display = '';
        } else {
            item.style.display = 'none';
        }
    });
}

// Function to handle play button
const PauseSong = () => {
    audioPlayer.pause();
    SwapSvg();
    //song_paused = true; 
    //playing_in_progress 
}
const StopSong = () => {
    audioPlayer.pause();
    audioPlayer.currentTime = 0;
};
const MuteSong = () => {

    if (!audioPlayer.muted) {
        audioPlayer.muted = true;
        muteBtn.innerHTML = "&#128263;";
        console.log("Is song muted..: " + audioPlayer.muted);
        return;
    } else {
        audioPlayer.muted = false;
        console.log("Is song muted..: " + audioPlayer.muted);
        muteBtn.innerHTML = "&#128266;";


    }

};
const ChangeSongsVolume = (event) => {
    audioPlayer.volume = event.target.value;
};
const ChangeSongsProgressBar = () => {
    const progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
    let minutes, seconds, m, s;
    progressBar.style.width = progress + '%';
    minutes = Math.round(audioPlayer.currentTime / 60);
    seconds = Math.round(audioPlayer.currentTime - minutes * 60).toString();
    m = Math.round(audioPlayer.duration / 60);
    s = Math.round((audioPlayer.duration - m) * 60).toString();
    current_time = audioPlayer.currentTime;
    if (s.length > 2) {
        s = s.substring(0, 2);
    }
    progressBarNumber.textContent = minutes + ":" + seconds + "/" + m + ":" + s;
    if (audioPlayer.duration != NaN) {
        id = (Math.random(0, 100) * 100).toString();
    }
};
const MakeSongClickable = (song) => {
    song.addEventListener('click', () => {
        //stop_playallfoward = true;

        //console.log(id);
        if (544 < 3) {
            console.log("__________________________________");
            console.log("Song Index..: " + GetSongIndex(song));
            console.log("Play Index..: " + play_index);
            console.log("Resumming At...: " + audioPlayer.currentTime);
            console.log("__________________________________");
            AudioPlay();
            return;
        }
        audioPlayer.src = song.getAttribute('data-src');
        playingSong.textContent = "Song..: " + song.textContent;
        AudioPlay();
        //audioPlayer.play();
        //stop_playallfoward = false;
        play_index = GetSongIndex(song);
        console.log("Playing index set to..: " + play_index);
        playing_in_progress = true;
        return;
    });
};
const GetSongIndex = (song) => {
    for (var item = 0; item < songsList.length; item++) {
        if (songsList[item].textContent == song.textContent) {
            return item;
        }
    }
    return 0;
};
const PlayBackwards = () => {
    play_index--;
    console.log("Play index..: " + play_index);
    if (play_aleatory) {
        Play(ShuffleIndex());
        return;
    }
    if (play_index == -1) {
        play_index = songsList.length - 1;
        Play(play_index);
        return;
    } else {
        Play(play_index);
        return;
    }

};
const PlayFoward = () => {
    play_index++;
    console.log("Play index..: " + play_index);
    if (play_aleatory) {
        Play(ShuffleIndex());
        return;
    }
    if (play_index >= songsList.length - 1) {
        play_index = 0;
        Play(play_index);
        return;
    } else {
        Play(play_index);
        return;
    }

};


const RepeatModeChange = () => {
    if (!song_repeat) {
        song_repeat = true;
        repeatMode.classList.remove("default");
        repeatMode.classList.add("action_type");
        console.log("Repeat song activated..: " + song_repeat);
        repeatMode.innerHTML = "&#x21BA;";
        return;
    } else {
        song_repeat = false;
        repeatMode.classList.remove("action_type");
        repeatMode.classList.add("default");
        //repeatMode.classList.add("switchable");
        console.log("Repeat song activated..: " + song_repeat);
        repeatMode.innerHTML = "&#10230;";
        return;
    }
};

const PlayAleatoryModeChange = () => {
    if (play_aleatory) {
        play_aleatory = false;
        aleatoryMode.classList.remove("action_type");
        aleatoryMode.classList.add("default");
        console.log("Aleatory song activated..: " + play_aleatory);
        //aleatoryMode.innerHTML = "&#x21BA;";
        return;
    } else {
        play_aleatory = true;
        aleatoryMode.classList.remove("default");
        aleatoryMode.classList.add("action_type");
        //aleatoryMode.classList.add("switchable");
        console.log("Aleatory song activated..: " + play_aleatory);
        //repeatMode.innerHTML = "&#10230;";
        return;
    }
};
/*
    Here are all the Events Listeners 
*/
// Fucntion to handle play previus song
playBack.addEventListener('click', () => PlayBackwards());
// Fucntion to handle play next song
playFoward.addEventListener('click', () => PlayFoward());
// Fucntion to handle repeat song
repeatMode.addEventListener('click', () => RepeatModeChange());
// Fucntion to handle aleatory play song
aleatoryMode.addEventListener('click', () => PlayAleatoryModeChange());
// Function to handle play PlaySong
playBtn.addEventListener('click', () => PlaySong());
// Secondary play button
//svg_icon0.addEventListener('click',()=>PlaySong());
// Secondary play button
//svg_icon1.addEventListener('click',()=>PlaySong());
// Function to handle pause button
pauseBtn.addEventListener('click', () => PauseSong());
// Function to handle stop button
//stopBtn.addEventListener('click',()=>StopSong());
// Function to handle mute button
muteBtn.addEventListener('click', () => MuteSong());
// Function to handle volume control
volumeControl.addEventListener('input', (event) => ChangeSongsVolume(event));
// Function to update progress bar
audioPlayer.addEventListener('timeupdate', () => ChangeSongsProgressBar());
// Function to handle song selection
songsList.forEach(song => { MakeSongClickable(song); });
// Attach search function to input event
searchInput.addEventListener('input', SearchSong);