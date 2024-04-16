const BOTKEY = '';
const client_name = '';

var timePerLetter = 40;
var newLineCharacter = '|';
function printOut(text) {
  var index = 0;
  document.getElementById("textbox").innerHTML='';
  var printNextLetter = function() {
    if (index < text.length) {
      var CHAR = text[index];

      switch(CHAR) {
        case newLineCharacter:
          document.getElementById("textbox").innerHTML = document.getElementById("textbox").innerHTML + '<br>';
          break;
        default:
          document.getElementById("textbox").innerHTML = document.getElementById("textbox").innerHTML + CHAR;
          break;
      }

      index++;

      setTimeout(printNextLetter, timePerLetter);
    }
  }
  printNextLetter()
}

function replaceKuki(msg) {
    return msg.replace(/Kuki/g, 'Mitsuku');
}

var audio = new Audio();
function playSong() {
    if (audio.paused) {
        var date = new Date().getUTCDate();
        var song = '';
        if (date%2==0) {
            song = '../sounds/mitsuku_anime1.wav';
        } else {
            song = '../sounds/mitsuku_anime2.wav';
        }
    
           audio.loop = true;
           audio.src = song;
           document.getElementById("musicButton").innerHTML = "MUSIC ON";
           audio.play();
    } else {
      document.getElementById("musicButton").innerHTML = "MUSIC OFF";
        audio.pause()
    }
    
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

var voiceOn = true;
function turnOffVoice() {
  if (voiceOn) {
    document.getElementById("voiceButton").innerHTML = "VOICE OFF";
    voiceOn = false;
  } else {
    document.getElementById("voiceButton").innerHTML = "VOICE ON";
    voiceOn = true;
  }
  
}

var voice = new Audio();
function playVoice() {
    if (voiceOn) {
      voice.src = '../sounds/voices/'+getRandomInt(10).toString()+'.wav';
      voice.play();
    }
    
}

function respond(user_text) {
    fetch('https://devman.kuki.ai/talk', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: 'botkey='+BOTKEY+'&client_name='+client_name+'&input='+user_text
}).then((response) => response.json()).then((data)=> printOut(replaceKuki(data["responses"][0])));    
  setTimeout(() => {
      playVoice();
    }, "500");
}

function cleartext()
{   
    respond(document.getElementById("chat_input").value);
    document.getElementById("lastMessageBox").value=document.getElementById("chat_input").value;

    document.getElementById("chat_input").value="";
    
}

const input = document.getElementById("chat_input");
input.addEventListener("keyup", (event) => {
  if (event.key === "Enter") {
    cleartext();
  }
});