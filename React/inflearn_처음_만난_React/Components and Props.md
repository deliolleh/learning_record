# Components and Props(☆)

### Components

- React => Component-Based Structure => 레고 블럭 조립하듯 Component들을 모아서 개발
- 컴포넌트들을 여러 번 사용함으로서 페이지를 완성하는 것 => 전체 코드 양 감소 => 유지 보수 비용 감소
- React Component는 JavaScript 함수와 개념적으로 비슷함(입력 => J.S function / React component => 출력)
- React: `Props => React Component => React element`
- React Component: 어떤 속성들을 입력으로 받아서 그에 맞는 리액트 엘리먼트를 생성해 리턴해주는 것
- React Element: React를 구성하는 가장 작은 Building Block, J.S 객체로 존재, 화면에 보이는 것을 기술



### Props

- (Property: *속성*/특성) => React Component의 속성
- Props ≒ 붕어빵에 들어가는 재료
- Component에 전달할 다양한 정보를 담고 있는 JavaScript 객체



### Props의 특징

- Read-Only: 값을 변경할 수 없다 => Like 붕어빵 다 굽고 속재료를 바꿀 수 없는 것처럼

- 다른 값으로 Element를 생성하려고 한다면? => 새로운 값(Props)을 Component에 전달해 새로운 Element 생성

- JavaScript 함수의 특성

  - `Pure function`: input을 변경하지 않으며, 같은 입력값에 대해서는 항상 같은 output을 return

    - ```javascript
      function sum(a, b) {
      	return a + b
      }
      ```

  - `Impure function`: 입력값을 변경

    - ```javascript
      function withdraw(account, amount) {
      	account.total -= amount;
      }
      ```

- React 공식 component 설명

  - All React components must act like *pure functions* with respect to their props.
  - 모든 리액트 컴포넌트는 그들의 Props에 관해서는 Pure 함수 같은 역할을 해야한다
  - 모든 리액트 컴포넌트는 Props를 직접 바꿀 수 없고, 같은 Props에 대해서는 항상 같은 결과를 보여줄 것!
  - **React Component의 Props는 바꿀 수 없고, 같은 Props가 들어오면 항상 같은 Element를 반환해야한다**



### Props 사용법

- JSX 사용(권장)

  - ```jsx
    function App(props) {
        return (
        	<Profile 
                name="Han"
                introduction="안녕하세요, Han입니다"
                <!-- 중괄호 사용 => JS 코드
    			문자열 이외의 정수, 변수 그리고 다른 컴포넌트 등이 들어갈 때에는
    			중괄호로 감싸 넣어야한다(문자열로 감싸도 된다)-->
                viewCount={1500}
            />
        )
    }
    ```

  - ```jsx
    <!-- 결과적으로 이런 형태가 된다 -->
    {
        name: "Han",
        introduction: "안녕하세요, Han입니다",
        viewCount: 1500
    }
    ```

  - ```jsx
    function App(prop) {
        return (
        	<Layout
                width={2560}
                height={1440}
    			<!-- Props에 중괄호를 사용해 Props의 값으로 Component를 넣을 수도 있다 -->
                header={
                	<Header title="Han의 블로그입니다." />
    	        }
                footer={
                	<Footer />
            	}
            />
        )
    }
    ```

- JSX 없이

  - ```react
    React.createElement(
    	type,
        <!-- props에 js 객체를 넣으면 해당 객체의 props가 됨 -->
        [props],
        [...children]
    )
    ```

  - ```react
    React.createElement(
    	Profile,
        {
            name: "Han",
            introduction: "안녕하세요 Han입니다",
            viewCount: 1500
        },
        <!-- 하위 component가 없으므로 null -->
        null
    )
    ```



### Component 만들기

#### Component 종류

- Class Component

  - 초기에 주로 사용

  - 사용하기 불편하다는 의견이 많음

  - J.S ES6에서의 Class을 사용해 만들어진 Component

  - Function Component에 비해 추가적인 기능을 가지고 있음(추후 다룸)

  - 모든 Class Component들은 `React.Component`를 상속받아 만들어짐

    ```react
    class Welcome extends React.Component {
        render() {
            return <h1>안녕, {this.props.name}</h1>
        }
    }
    ```

    

- Function Component

  - 개선한 이후 사용

  - 개선하는 과정에서 개발된 것이 **Hook**

  - 간단한 코드를 가짐

    ```react
    function Welcome(props) {
        return <h1>안녕, {props.name}</h1>;
    }
    ```



#### Component의 이름

- **Component의 이름은 항상 대문자로 시작해야한다** => 소문자로 시작하는 컴포넌트들을 DOM tag로 인식

- div, span => 내장 컴포넌트, DOM 컴포넌트/ `React.createElement('div')` 같은 형태로 전달

- Foo => `React.createElement(Foo)` 형태로 컴파일/ J.S 파일에서 사용자가 정의했거나 import한 컴퍼넌트들을 가리킴

- ex)

  - HTML `div`로 인식

    ```react
    const element = <div />;
    ```

  - `Welcome`이라는 React Component로 인식

    ```react
    const element = <Welcome name="인제" />;
    ```

    

#### Component 렌더링

- Component가 실제로 화면에 렌더링 되는 것은 아님

- Component를 통해 만들어진 Element가 실제로 화면에 나타나는 것

- 렌더링의 시작은  Component로부터 Element를 만들어야함

  - DOM tag를 사용한 element

    ```react
    const element = <div />;
    ```

  - 사용자가 정의한 Component를 사용한 element

    ```react
    const element = <Welcome name="인제" />;
    ```

    ```react
    function Welcome(props) {
        return <h1>안녕, {props.name}</h1>;
    }
    
    const element = <Welcome name="인제" />;
    ReactDOM.render(
        element,
        document.getElemntById('root')
    )
    ```

    

#### Component 합성

- 여러 개의 Component들을 합쳐 하나의 Component로 만드는 것

- 복잡한 화면을 여러 개의 Component로 나눠서 구현 가능

  ```react
  function Welcome(props) {
      return <h1>Hello, {props.name}</h1>
  }
  
  function App(props) {
      return (
      	<div>
          	<Welcome name="Mike" />;
              <Welcome name="Steve" />;
              <Welcome name="Jane" />;
          </div>
      )
  }
  
  ReactDOM.render(
      <App />,
      document.getElmentById('root')
  )
  ```

  

#### Component 추출

- 복잡한 Component들을 쪼개 여러 개의 Component로 나눈 것

- 추출을 잘 활용하면 재사용성이 증가한다 => Component의 크기가 작아질수록 기능과 목적이 명확해지고, Props도 단순해지기 때문에 다른 곳에서 사용할 수 있는 확률이 증가 => 개발 속도도 상승

- ex)

  - 기존

    ```react
    function Comment(props) {
        return (
        	<div className="comment">
            	<div className="user-info">
                	<img className="avator"
                        src={props.author.avatarUrl}
                        src={props.author.name}
                    />
                    <div className="user-info-name">
                        {props.author.name}
                    </div>
                </div>
                
                <div className="comment-text">
                	{props.text}
                </div>
                
                <div className="comment-date">
                	{formatDate(props.date)}
                </div>
            </div>
        );
    }
    ```

    위의 함수에서의 Props

    ```react
    props = {
        author: {
            name: "소플",
            avatarUrl: "https://...",
        },
        text: "댓글입니다",
        date: Date.now(),
    }
    ```

    - Avatar 추출하기

    ```react
    function Avatar(props) {
    	return (
        	<img className="avatar"
                // author보다 좀 더 보편적인 user사용 => 재사용성 고려
                src={props.user.avatarUrl}
                src={props.user.name}
        )
    }
    ```

    - Avatar 컴포넌트가 적용된 모습

    ```react
    function Comment(props) {
        return (
        	<div className="comment">
            	<div className="user-info">
                	<Avatar user={props.author} />
                    <div className="user-info-name">
                        {props.author.name}
                    </div>
                </div>
                
                <div className="comment-text">
                	{props.text}
                </div>
                
                <div className="comment-date">
                	{formatDate(props.date)}
                </div>
            </div>
        );
    }
    ```

    - userInfo 추출

    ```react
    function UserInfo(props) {
        return (
        	<div className="user-info">
            	<Avatar user={props.user} />
                <div className="user-info-name">
                	{props.user.name}
                </div>
            </div>
        );
    }
    ```

    - userInfo 반영

    ```react
    function Comment(props) {
        return (
        	<div className="comment">
            	<UserInfo user={props.author} />            
                <div className="comment-text">
                	{props.text}
                </div>
                
                <div className="comment-date">
                	{formatDate(props.date)}
                </div>
            </div>
        );
    }
    ```

    

- 재사용이 가능한 Component를 많이 가지고 있을수록 개발 속도가 빨라진다

  