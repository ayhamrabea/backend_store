async function cartUpdate(e) {
    const {data} = await axios(e.dataset.url)
    const {massage , intms_count} = data
    notyf.success({
        massage,
        dismissible: true,
        icon:false
    })
    
    document.getElementById('cart-items-count').innerHTML = intms_count

}



async function cartdemove(e) {
    await axios(e.dataset.url)
    location.reload()
    
}