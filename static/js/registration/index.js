function updatePreview(input, target) {
    let file = input.files[0];
    let reader = new FileReader();

    reader.readAsDataURL(file);
    reader.onload = function () {
        let img = document.getElementById(target);
        // can also use "this.result"
        img.src = reader.result;
    }
}

function getRole(lang = 'ru'){
    const splittedPath = window.location.href.split('/')
    const roles = {
        'runner':'бегун',
        'sponsor':'спонсор',
        'coordinator':'координатор'
    }
    const role = roles[splittedPath.slice(-2,-1)]
    if (role == undefined){
        window.location.href = '/'
    }
    if(lang === 'ru'){
        return role
    }else if (lang === 'en'){
        return splittedPath.slice(-2,-1)
    }
}


async function submit(event){
    event.preventDefault()

    const formData = new FormData(event.target)
    formData.append('role', getRole('en'))
    await fetch('', {
        method:"POST",
        body:formData
    })
    // window.location = '/'
}
const roleElement = document.querySelector('.role')
roleElement.innerHTML = `Регистрация для роли "${getRole()}"`

document.getElementById("sign-up")
    .addEventListener('submit', submit)