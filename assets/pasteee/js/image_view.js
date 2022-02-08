/*
 *   Copyright (c) 2022 
 *   All rights reserved.
 */

let copy_link = document.getElementById("get-link");


copy_link.onclick = (evt) => {

    navigator.clipboard.writeText(window.location.href)
    .then((e) => {
        M.toast({html: 'link copied!'});
    });

};
