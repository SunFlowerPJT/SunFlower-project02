document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username && password) {
        alert("로그인 성공!");
    } else {
        alert("아이디와 비밀번호를 입력해주세요.");
    }
});
