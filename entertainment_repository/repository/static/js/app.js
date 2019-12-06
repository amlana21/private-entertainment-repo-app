
console.log('loaded')

// console.log(window.location.pathname)
const pth=window.location.pathname




    let tmpval=$('#srchVal').val()
    if (pth.includes('searchitems')){
             console.log('hhhhhhh')
             $('#srchVal').focus().val("").val(tmpval);
             const rwTbl=document.querySelectorAll('.rslttbl')
            // const rwTbl=document.querySelectorAll('.tabcntnt')
            let divCnt=0
            for(i=0;i<rwTbl.length;i++){

                // console.log($(rwTbl[i]).prop('id'))
                let tblId=$(rwTbl[i]).prop('id')
                let divId=''
                
                // console.log($(`#${tblId} tr`).length)
                if($(`#${tblId} tr`).length>1){
                    // console.log(tblId.split('-')[1])
                    divId=tblId.split('-')[1]
                    break
                    // return
                }
                divCnt++
            }
            
             const navitems=document.querySelectorAll('.itemnavlinks')
             const navCntnt=document.querySelectorAll('.tabcntnt')

             navitems[divCnt].classList.add('active')
             navCntnt[divCnt].classList.add('active')
             navCntnt[divCnt].classList.remove('fade')
            
         }else{
            const navitems=document.querySelectorAll('.itemnavlinks')
            const navCntnt=document.querySelectorAll('.tabcntnt')

            navitems[0].classList.add('active')
            navCntnt[0].classList.add('active')
            navCntnt[0].classList.remove('fade')
         }

$('#addbutton').on('click',()=>{
    $('#addmodal').show()
})

