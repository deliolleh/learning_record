import React from "react";
import Comment from "./Comment";

const comments = [
    {
        name: "이인제",
        comment: "안녕하세요, Han입니다.",
    },
    {
        name: "유재석",
        comment: "리액트 나쁘지 않아요",
    },
    {
        name: "강민경",
        comment: "리액트 해볼까요?",
    },
];

function CommentList(props) {
    return (
        <div>
            {comments.map((comment) => {
                return (
                    <Comment name={comment.name} comment={comment.comment} />
                );
            })}
        </div>
    )
}

export default CommentList;