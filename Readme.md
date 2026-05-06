# FAST API BLOG CRUD

## Giới thiệu 
Fast API là một python web framework giúp chúng ta có thể xây dựng API cho website, Mobile app với python.

## Mục đích
Học những thứ cơ bản để viết Api bằng python, biết query bảng dữ liệu, mối quan hệ các bảng 1-1, 1-n, n-n.
Xây dựng hệ thống API với mô hình MVC + Service Layer.
Tối ưu hóa và trãi nghiệm người dùng.
Biết xài Swagger viết doc cho API.

## Công nghệ sử dụng.
Backend: FastAPI, PosgreSQL, Render (productions env).

Frontend: ReactJS, Redux, Tailwindcss, ShacnUI, Vercel (productions ENV)

## Công cụ
Code editor: Vs Code
Client PG: PG admin 4.
=> Sau nay sẽ chuyễn dự án sang DOCKER và xài K8S.

## Cấu trúc thư mục 
blog-api/
│── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── config.py        # load ENV
│   │
│   ├── db/
│   │   ├── session.py       # connect DB
│   │   └── base.py          # Base model
│   │
│   ├── models/
│   │   └── post.py          # DB model
│   │
│   ├── schemas/
│   │   └── post.py          # request/response schema
│   │
│   ├── services/
│   │   └── post_service.py  # business logic
│   │
│   ├── api/
│   │   └── v1/
│   │       └── post.py      # routes
│   │
│   ├── dependencies/
│   │   └── db.py
│   │
│   └── utils/
│       └── helper.py        # custom functions
│
│── .env
│── requirements.txt