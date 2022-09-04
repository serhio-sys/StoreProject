const item = document.querySelector('.item_')
const input = document.getElementById('item')
const url = window.location.href
const form = document.getElementById('form-s')
const results = document.getElementById('results')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value



const sendSearchData = (item) => {
  $.ajax({
      type: "POST",
      url: 'search/',
      data: {
        'csrfmiddlewaretoken':csrf,
        'item':item
      },
      success: (res) => {
        console.log(res.data)
        const data = res.data
        if (Array.isArray(data)){
          
          results.innerHTML = ''
          data.forEach(item=>{
            results.innerHTML += `
            <div class="item_">
            ${item}  
            </div>
            `
          })
        }
        else{
          if(input.value.length > 0){
            results.innerHTML = `<b>${data}</b>`
          }
          else{
            results.classList.add('not_vis')
            results.innerHTML = ""
          }
        }
      },
      error: (err) => {
        console.log(err)
      }
  })
}

input.addEventListener('keyup', e => {
  console.log(e.target.value)

  if (results.classList.contains('not_vis')){
    results.classList.remove('not_vis')
  }

  sendSearchData(e.target.value)
})  