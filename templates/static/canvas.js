
$('.popup').hide();


window.onload = function()
{
draw()
}

$(function(){
    $('tr[data-href]', 'table.table-clickable').on('click', function(){
      location.href = $(this).data('href');
    });
  });

  var the_json = JSON.parse('{{qs_json|escapejs}}');

  $('.chara').on('click', function(){
              var nameVal = $(this).children('td')[0].innerText;
              // alert(' name: '+ nameVal);
              $('.popup').show();
              for(let i in the_json) {
              //  console.log(the_json[i]);
               if(the_json[i].title==nameVal){
                $('.popup').html('<p>物品名:'+the_json[i].title+'</p>'+
                  '<p>id:'+the_json[i].id+'</p>'+
                 '<p>最終検知時刻:'+the_json[i].duedate+'</p>'+
                 '<p>予定:A社 7F</p>'+
                 '<p>実績:A社 6F</p>'+
                 '<canvas id="canvas" width="600" height="500"  style="background-color:yellow;"></canvas>'
                 );
               }
              // $('.popup').text(the_json[1].id);
              }
              draw()
  
              });
    


  