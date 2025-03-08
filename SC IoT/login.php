<?php 
session_start(); 
session_unset(); 
include 'koneksi.php'; 
?> 

<link rel="stylesheet" href="login.css?d=<?php echo time(); ?>" /> 

<!DOCTYPE html> 
<html> 
<head> 
<title> Halaman Login </title> 
</head> 

<body>  
<div class="center"> 
    <center><h1> Login Dulu Yukss </h1> </center> 

    <div id="container"> 
        <form action="" method="post"> 
            <label for="username"> Masukkan username: </label> 
            <input type="text" name="user" placeholder="Masukkan username" value ="" /> <br> 
            
            <label for="password"> Masukkan Password: </label> 
            <input type="password" name="pass" placeholder="Masukkan password" /> <br> 
            <input type="submit" name="login" value="login" /> <br> 
        </form> 

        <?php 
        if (isset($_POST['login'])){ 
            $user = $_POST['user'];  
            $pass = $_POST['pass']; 

            $data_user = mysqli_query($conn, "SELECT * FROM user WHERE username='$user' AND password='$pass'"); 
            $r = mysqli_fetch_array($data_user); 
            $username = $r['username']; 
            $password = $r['password']; 
            $level = $r['level']; 
            
            if ($user == $username && $pass == $password){ 
                $_SESSION['level'] = $level; 
                $_SESSION['username'] = $user; 
                header('location:index.php'); 
            } else { 
                echo "Gagal Login<br/>"; 
            } 
        } 
        ?> 
    </div> 
</body> 
</html>