console.log("성공!");

window.onload=function(){
   get_posting();
}
//window.open('index.html','width=2000px,height=1500')팝업창 크기조절은 윤지씨

    function get_moive(){
     $.ajax({
        type: "GET",
        url: "/post",
        data: {},
        success: function(result){
            console.log(result);
            if(result["result"] == 'success'){
                alert("성공!")
                window.location.reload(true);
            }else{
                alert("실패 하였습니다.")
            }
          }
        })
    }

     function get_posting() {
       $.ajax({
          type: "GET",
          url: "/post",
          data: {},
          success: function(response){
            let moives = response['articles'];
            console.log(moives);
            for (let i = 0 ; i < moives.length; i++) {
              let url = moives[i]['url'];
              let title = moives[i]['title'];
              let directors = moives[i]['directors'];
              let actors = moives[i]['actors'];
              let dates = moives[i]['dates'];
              let subtitle = moives[i]['subtitle'];
              let story = moives[i]['story'];

              make_card(title,directors,actors,dates,subtitle,story);
            }
          }
        })
     }
      function make_card(url,comment,title,image,description) {
        $('#post-cards').append('<div class="pop">\
            <div class="pop">\
              <p class="title">'+description+'</p>\
              <p class="directors">'+description+'</p>\
              <p class="actors">'+description+'</p>\
              <p class="dates">'+comment+'</p>\
              <p class="subtitle">'+comment+'</p>\
              <p class="story">'+comment+'</p>\
            </div>\
          </div>');
      }
//    창닫기
    function MovePage() {
        window.opener.top.location.href="연결할파일"
        window.close()
    }
