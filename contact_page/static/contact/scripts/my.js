$(".navbar-nav .nav-link").on("click", function () {
    $(".navbar-nav ").find(".active").removeClass("active");
    $(this).addClass("active");
});

$(window).on('load',function(){
    $('.preloader').addClass('complete')
    setTimeout(function () {
        $('.preloader').addClass('finished')
        $('.loading').removeClass('loading')
        $('.typewriter').addClass('start')
        
    }, 1000)
    setTimeout(function () {
    $('.loading-nav').removeClass('loading-nav')
    },850)

})

function countLines() {
    const navHeight = 0;
    const footHeight = 0;
    const lineHeightInt = 1.2;
    const lineHeightEm = lineHeightInt + 'em';
    const lineHeightInt2 = lineHeightInt+0.1;
    const lineHeightEm2 = lineHeightInt2+'em'
    const lineHeightPx = lineHeightInt * 16;
    const padding = 1;  // 1px
    const letterSpace = 0.4107;
    const letterHeight = lineHeightPx + padding + letterSpace;
    $('#code').css('line-height', lineHeightEm);
    $('#ul-code').css('font-size', lineHeightEm);
    $('#ul-r-code').css('font-size', lineHeightEm2);
    var el = document.getElementById('content');
    var divHeight = el.offsetHeight - navHeight - footHeight;
    lines = Math.ceil((divHeight / letterHeight));
    // alert("lines:"+lines);
    document.getElementById('code').style.height = divHeight + 'px';
    var ul = document.getElementById("ul-code");
    // var ul_r = document.getElementById("ul-r-code")
    for (var i = 1; i <= lines; i++) {
        var li = document.createElement('li');
        // var li_r = document.createElement('li');

        // if (i == 1) {
        //     li_r.appendChild(document.createTextNode(i));
        // }
        // else {
        //     li_r.appendChild(document.createTextNode(i));
        // }
        li.appendChild(document.createTextNode(i));
        ul.appendChild(li);
        // ul_r.appendChild(li_r)

    }
}
$(window).on('load',function (){
    countLines();
})

$(window).resize(function () {
    var ul = document.getElementById("ul-code");
    var ul_r = document.getElementById("ul-r-code")
    ul.innerHTML = '';
    ul_r.innerHTML= '';
    countLines();
})


function setupTypewriter(t) {
    var HTML = t.innerHTML;

    t.innerHTML = "";

    var cursorPosition = 0,
        tag = "",
        writingTag = false,
        tagOpen = false,
        typeSpeed = 130,
        tempTypeSpeed = 0;

    var type = function () {

        if (writingTag === true) {
            tag += HTML[cursorPosition];
        }

        if (HTML[cursorPosition] === "<") {
            tempTypeSpeed = 0;
            if (tagOpen) {
                tagOpen = false;
                writingTag = true;
            } else {
                tag = "";
                tagOpen = true;
                writingTag = true;
                tag += HTML[cursorPosition];
            }
        }
        if (!writingTag && tagOpen) {
            tag.innerHTML += HTML[cursorPosition];
        }
        if (!writingTag && !tagOpen) {
            if (HTML[cursorPosition] === " ") {
                tempTypeSpeed = 0;
            }
            else {
                tempTypeSpeed = (Math.random() * typeSpeed) + 50;
            }
            t.innerHTML += HTML[cursorPosition];
        }
        if (writingTag === true && HTML[cursorPosition] === ">") {
            tempTypeSpeed = (Math.random() * typeSpeed) + 50;
            writingTag = false;
            if (tagOpen) {
                var newSpan = document.createElement("span");
                t.appendChild(newSpan);
                newSpan.innerHTML = tag;
                tag = newSpan.firstChild;
            }
        }

        cursorPosition += 1;
        if (cursorPosition < HTML.length - 1) {
            setTimeout(type, tempTypeSpeed);
        }

    };

    return {
        type: type
    };
}

var typer = document.getElementById('typewriter');

typewriter = setupTypewriter(typewriter);

typewriter.type();


$(document).ready(function () {
    // show the alert
    setTimeout(function () {
        $(".alert").alert('close');
    }, 5000);
});