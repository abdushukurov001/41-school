let TOKEN ='7362615665:AAEZRbtp_3tqhtRlzPub4Wvt1ZwkBMigK4U';
let CHAT_ID= -1002496843835;
let URL_API = `https://api.telegram.org/bot${ TOKEN}/sendMessage`;


document.getElementById('tg').addEventListener('submit',function(e){
   e.preventDefault();

   let message= `<b>Ro'yxat</b>\n`;
   message+= `<b>Ism:</b> ${this.name.value}\n`;
   message+= `<b>Raqam:</b> ${this.number.value}\n`;


   
   console.log(message);


  axios.post(URL_API,{
    chat_id:CHAT_ID,
    parse_mode: 'html',
    text: message
  })
  .then((res)=>{
    this.name.value = '';
    this.number.value = '';

  })
  .catch(()=>{
    console.warn(err)
  })
  .finally(()=>{
   console.log('tugadi')
  })
})



function scrollToSection(id) {
  const element = document.getElementById(id);
  if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });

  } else {
      console.warn(`Section with id ${id} not found`);
  }
}


