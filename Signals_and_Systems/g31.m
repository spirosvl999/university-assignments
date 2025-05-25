fs = 8000;
Dt = 0.4;
Notes_Array = ['A ';'A#';'B ';'C ';'C#';'D ';'D#';'E ';'F ';'F#';'G ';'G#'];

for i = 1:1:length(Notes_Array)
        sound(g3function(Notes_Array(i,1:end),Dt,fs,1));
        sound(0);
end
