# Rendering Elements

### Elements란?

- Elements: 요소/성분
- React에서의 Elements => React를 구성하는 요소
- React 공식 정의: **Elements** are **the smallest building blocks** of React apps
- 리액트 앱을 구성하는 가장 작은 블록들
- DOM Element vs React Element
  - DOM Elements: HTML 요소들을 나타냄/ React Elements에 비해 크고 무거움
  - Descriptor(기술): 화면에 나타나는 내용을 기술하는 JS 객체 => DOM과의 통일성을 위해 Element라고 부르게 됨
  - React Elements: DOM Element의 가상 표현(Virtual DOM) / 강의에서의 Element는 기본적으로 React Element를 의미
- **즉 Elements는 화면에서 보이는 것을 기술**



### Element의 생김새

- React Element는 JS 객체 형태로 존재
- Element는 컴포넌트의 유형과 속성 및 내부의 모든 자식에 대한 정보를 포함하고 있는 일반적인 JS 객체
- React Elements들은 불변성을 가지고 있음 => 한 번 생성되면 바뀔 수 없음

- CreateElement의 구성요소
  - type: HTML tag 이름이 문자열로 들어가거나 또다른 ReactElement가 들어감 => HTML tag가 됨
    - 또다른 React Componenet를 넣는다면? => 어짜피 마지막엔 HTML tag가 되고 이들은 자식 Element가 됨
  - props: Element의 속성 => `class/style` / attribute의 상위 속성
  - children: 해당 Element의 자식 Element



- **React Element는 우리 눈에 보이는 것을 기술한다**



### Element의 특징

- 불변성: React Elements are immutable / 변하지 않는다
- **Elements 생성 후**에는 children이나 attributes를 바꿀 수 없다 => 혹시 화면 갱신이 되지 않는 것인가?
- Component(붕어빵 틀) - Element(붕어빵) => Element의 불변성을 이해할 수 있는 방법
- 화면에 변경된 Element를 보여주는 방법: 기존 Element를 변경하는 것 X => 새로운 Element를 만들고 바꿔치기(why? React의 장점: 빠른 렌더링 속도 => Virtual DOM)