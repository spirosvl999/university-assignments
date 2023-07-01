
let questions = [
    {
        id: 1,
        question: 'What this code does? \n int main\n {\n list<int> myList(1, 2);\n return 0;\n }'
		,
        answer:"Create",
        options: [
            "Create",
            "Remove",
            "Input",
			"Show"
        ]   
    },
    {
        id: 2,
        question: "What does\n mylist.push_front(11);\n do?",
        answer: "Insert at the start of the List number 11",
        options: [
          "Removes number 11 from the start of the List",
          "Insert at the end of the List number 11",
          "Insert at the start of the List number 11",
          "None of these"
        ]
      },
      {
        id: 3,
        question: "What \n list<int>::iterator i = mylist.begin(); \n my_list.erase(i); \n do?",
        answer: "Removes first number of the List",
        options: [
          "Shows the list",
          "Shows the first number of the list",
          "Removes last number of the List",
          "Removes first number of the List"
        ]
      },
];

let question_count = 0;
let points = 0;


window.onload = function(){
    show(question_count);
};

function show(count){
    let question = document.getElementById("questions");
    let[first, second, third, fourth] = questions[count].options;

    question.innerHTML = `<h2>Q${count + 1}. ${questions[count].question}</h2>
    <ul class="option_group">
    <li class="option">${first}</li>
    <li class="option">${second}</li>
    <li class="option">${third}</li>
    <li class="option">${fourth}</li>
    </ul>`;
    toggleActive();  
}

function toggleActive(){
    let option = document.querySelectorAll("li.option");
    for(let i=0; i < option.length; i++){
        option[i].onclick = function(){
            for(let i=0; i < option.length; i++){
                if(option[i].classList.contains("active")){
                    option[i].classList.remove("active");
                }
            }
            option[i].classList.add("active");
        }
    }
}

function next(){

    if(question_count == questions.length -1){
        location.href = "final.html";
    }
    console.log(question_count);


let user_answer = document.querySelector("li.option.active").innerHTML;

if(user_answer == questions[question_count].answer){
    points += 1;
    sessionStorage.setItem("points",points);
}
console.log(points);

question_count++;
show(question_count);
}