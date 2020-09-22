function changeTemplate(){
    if($('input:radio[id=square]').is(':checked')){
        $('#square_div').show();
        $('#circle_div').hide();
        $('#heart_div').hide();
        $('#animal_div').hide();

        $('#color_option').show();
        $('#animal_option').hide();
    }else if($('input:radio[id=circle]').is(':checked')){
        $('#square_div').hide();
        $('#circle_div').show();
        $('#heart_div').hide();
        $('#animal_div').hide();

        $('#color_option').show();
        $('#animal_option').hide();
    }else if($('input:radio[id=heart]').is(':checked')){
        $('#square_div').hide();
        $('#circle_div').hide();
        $('#heart_div').show();
        $('#animal_div').hide();

        $('#color_option').show();
        $('#animal_option').hide();
    }else{
        $('#square_div').hide();
        $('#circle_div').hide();
        $('#heart_div').hide();
        $('#animal_div').show();

        $('#color_option').hide();
        $('#animal_option').show();
    }
}

function fnMore(){
    if(firstReport.style.display=='none'){
        $('#firstReport').show();
        show.innerText='접기...';
    }else{
        $('#firstReport').hide();
        show.innerText='더보기...';
    }
}
function fnMore2(){
    if(secondReport.style.display=='none'){
        $('#secondReport').show();
        show2.innerText='접기...';
    }else{
        $('#secondReport').hide();
        show2.innerText='더보기...';
    }
}
function fnMore3(){
    if(thirdReport.style.display=='none'){
        $('#thirdReport').show();
        show3.innerText='접기...';
    }else{
        $('#thirdReport').hide();
        show3.innerText='더보기...';
    }
}

function youtubeMore(){
    if(moreyoutube.style.display=='none'){
        $('#moreyoutube').show();
        youtubeshow.innerText='추천 음악 접기';
    }else{
        $('#moreyoutube').hide();
        youtubeshow.innerText='추천 음악 더 듣기';
    }
}
