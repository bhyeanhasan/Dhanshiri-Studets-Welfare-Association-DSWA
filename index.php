python manage.py runserver 0.0.0.0:8000

<?php
include 'Database/Connection.php';
include 'Template/htmlHeader.php';
session_start();
?>

<!--navbar-->
<nav class="navbar navbar-expand-lg navbar-light bg-light">

    <a class="navbar-brand" href="#">
        <?php
        if(isset($_SESSION['user']))
            echo $_SESSION['user'];
        else
            echo ""
        ?>
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">

            <?php if(! isset($_SESSION['id'])): ?>
                <li class="nav-item">
                    <a class="nav-link" href="Template/loginPage.php">Login <span class="sr-only">(current)</span></a>
                </li>

            <?php else: ?>
                <li class="nav-item">
                    <a class="nav-link" href="view/TeacherStudent.php">Admin Panel</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="view/profile.php">Profile</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="Auth/logout.php">Logout</a>
                </li>
            <?php endif; ?>

        </ul>
    </div>
</nav>
<!--end navbar-->

<!--slider-->
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img class="d-block w-100" src="Static/image/one.jpg" alt="First slide" style="height: 80vh">
            <div class="carousel-caption d-none d-md-block">
                <h4>আমাকে একটি শিক্ষিত মা দেও <br> আমি তোমাদের একটি শিক্ষিত জাতি দেব</h4>
                <p>-নেপোলিয়ন</p>
            </div>

        </div>
        <div class="carousel-item">
            <img class="d-block w-100" src="Static/image/two.jpg" alt="Second slide" style="height: 80vh">
            <div class="carousel-caption d-none d-md-block">
                <h4>শিক্ষাই জাতির মেরুদন্ড</h4>
                <p>মির্জাপুর, পোনাবালিয়া, ঝালকাঠি</p>
            </div>
        </div>
        <div class="carousel-item">
            <img class="d-block w-100" src="Static/image/one.jpg" alt="Third slide" style="height: 80vh">
            <div class="carousel-caption d-none d-md-block">
                <h4>শিক্ষাই জাতির মেরুদন্ড</h4>
                <p>মির্জাপুর, পোনাবালিয়া, ঝালকাঠি</p>
            </div>
        </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>
<!--end slider-->

<div class="container-fluid">
    <div class="row">
        <div class="col-md-8">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <h4 class="text-center">নোটিশ</h4>
                        <img src="Static/image/one.jpg" class="w-100">
                    </div>

                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <h4 class="text-center">প্রধান শিক্ষকের বানী</h4>
                        <img src="Static/image/one.jpg" class="w-100">
                    </div>

                </div>
            </div>

        </div>
    </div>
</div>

<?php
include "Template/htmlFooter.php";
?>


