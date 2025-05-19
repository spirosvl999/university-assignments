# Signals and Systems

This repository contains both **code** and **mathematical solutions** related to the course *Signals and Systems*.

Inside this repo we have solutions for **Γ1, Γ2, Γ3 & Γ4** of book.

---

## 📘 Mathematical Solutions

Some exercises required analytical/mathematical solutions rather than code. These solutions are included in this README file.

### Θέμα Γ.1  
**A)** Σήμα συνεχούς χρόνου:  
&nbsp;&nbsp;&nbsp;&nbsp;*x(t) = cos(100πt) + cos(200πt) + sin(500πt)*  

Για το παραπάνω σήμα έχουμε:  
- f₁ = 50 Hz  
- f₂ = 100 Hz  
- f₃ = 250 Hz  
(δεδομένου ότι ω = 2πf)

Άρα, σύμφωνα με το θεώρημα **Whittaker-Shannon-Nyquist**:  
&nbsp;&nbsp;&nbsp;&nbsp;*fs = 2 × fmax = 2 × 250 = 500 Hz*  
ή ισοδύναμα:  
&nbsp;&nbsp;&nbsp;&nbsp;*Ts = 1 / fs = 0.002 sec*

**ΣΤ)** Παρατηρούμε ότι όσο αυξάνεται η συχνότητα δειγματοληψίας (*fₛ*) το δείγμα γίνεται πιο ξεκάθαρο, ενώ όσο μειώνεται η *fₛ* αρχίζει να χάνει την ευκρίνειά του.  
Με *Ts = 0.001* παίρνω τα καλύτερα δείγματα (δλδ μικρότερο βήμα από το αρχικό *Ts*).  
Προηγουμένως, τα σήματα συνέπιπταν το ένα πάνω στο άλλο — το ένα με μικρότερη και το άλλο με μεγαλύτερη συχνότητα — γεγονός που εξηγεί την αλλαγή στα χρώματα και στο *Ts*.

---

## 💻 Code (Matlab)

Coding was done using **Matlab**, and each script is named using the format `G.number.number`, corresponding to the exercise number.

All code files are uploaded and organized accordingly.