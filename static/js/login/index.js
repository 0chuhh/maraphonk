function closeAlert(event) {
    console.log(this)
    event.target.parentNode.parentNode.remove()
}


async function submit(event) {
    event.preventDefault()
    try {

        let ban = JSON.parse(localStorage.getItem('ban'))
        if (ban.seconds != 0) {
            ban.seconds += 15
            alert(`BAN ${ban.seconds} secs`)
            localStorage.setItem('ban', JSON.stringify(ban))
            checkBan()
        } else {
            const formData = new FormData(event.target)
            const response = await fetch('', {
                method: "POST",
                body: formData
            }).then((response) => {
                return response.text();
            }).then((html) => {
                if(html == 'error'){
                    let ban = JSON.parse(localStorage.getItem('ban'))
                    ban.seconds += 15
                    localStorage.setItem('ban', JSON.stringify(ban))
                    checkBan()
                if (ban.seconds != 0) {
                    alert(`BAN ${ban.seconds} secs`);
                }
                }else{
                document.body.innerHTML = html
                }
            });
        }

    } catch (e) {

    }

    // window.location = '/'
}
let interval
function checkBan(){

if(localStorage.getItem('ban') == undefined){
    localStorage.setItem('ban', JSON.stringify({seconds:0}))
}
else if(JSON.parse(localStorage.getItem('ban')).seconds != 0){
    setInterval(()=>{
        let ban = JSON.parse(localStorage.getItem('ban'))
        if(ban.seconds>0){
            ban.seconds -= 1
            localStorage.setItem('ban', JSON.stringify(ban))
        }
    },1000)
}
}
checkBan()


document.getElementById("login")
    .addEventListener('submit', submit)