var tb = document.getElementById("queryLeftTable");
var rows = tb.children; 
var train_number = ["G105"];
var passenger_num = 2; 
var seat_level = [2,3];
for (var i = rows.length - 1; i >= 0; i--) {
	var tr = rows[i];
	var number = tr.children[0].children[0]
	.children[0].children[0].textContent;
	if(train_number.indexOf(number)==-1)
		continue;
	for (var i = seat_level.length - 1; i >= 0; i--) {		
		if(tr.children[seat_level[i]].textContent == '有'){
			tr.lastElementChild.firstChild.click();
		}
		if(tr.children[seat_level[i]].textContent >=passenger_num){
			tr.lastElementChild.firstChild.click();
		}
	}
}

